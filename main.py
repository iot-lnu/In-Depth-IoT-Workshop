import time
import ujson
import constants as CONST
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom
from machine import Pin

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(1)

temp_topic = CONST.DATACAKE_MQTT_TOPIC + "TEMPERATURE"
humi_topic = CONST.DATACAKE_MQTT_TOPIC + "HUMIDITY"

while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        print("Not valid")
        result = th.read()

    temperature = result.temperature
    humidity = result.humidity

    print('Temperature:', temperature, 'Humidity:', humidity)

    client.publish(topic=temp_topic, msg=str(temperature))
    time.sleep(0.1)
    client.publish(topic=humi_topic, msg=str(humidity))

    time.sleep(60)
