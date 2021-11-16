# Data is sent to Pybytes. Needs to flashed with Pybyte firmware
import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom
import struct


# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin(‘P23’, mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)


while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    temp = result.temperature
    humidity = result.humidity

    print(‘Temp:’, temp)
    print(‘RH:‘, humidity)
    #pybytes.send_signal(1,result.temperature)
    #pybytes.send_signal(2,result.humidity)

    package = struct.pack(‘>bB’, int(temp), int(humidity))
    s.send(package)

    time.sleep(5)
