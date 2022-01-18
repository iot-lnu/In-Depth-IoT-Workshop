from network import WLAN
from mqtt import MQTTClient
import ubinascii
import constants as CONST
import machine

# WiFi Setup
client_id = ubinascii.hexlify(machine.unique_id())
print(client_id)
wlan = WLAN(mode=WLAN.STA)
wlan.connect(CONST.WIFI_SSID, auth=(WLAN.WPA2, CONST.WIFI_PASS), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print('Connected to WiFi\n')

# MQTT Setup
def sub_cb(topic, msg):
   print(msg)

client = MQTTClient(client_id,
                    CONST.DATACAKE_MQTT_URL,
                    user=CONST.DATACAKE_TOKEN,
                    password=CONST.DATACAKE_TOKEN,
                    port=CONST.DATACAKE_MQTT_PORT)

client.set_callback(sub_cb)
client.connect()
print('connected to MQTT server')
