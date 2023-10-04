from network import LoRa
import socket
import time
import ubinascii

app_eui = '0000000000001234'
dev_eui = '70B3D57ED00617EA'
app_key = 'A63A0CD9EC46317A2E11B74D93C08E56'


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify(app_eui)
dev_eui = ubinascii.unhexlify(dev_eui)
app_key = ubinascii.unhexlify(app_key)

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)
