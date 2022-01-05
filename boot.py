from network import LoRa
import binascii
print("#################################")
print(binascii.hexlify(LoRa().mac()).upper())
print("#################################")

from network import LoRa
import socket
import time
import ubinascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('BE02CDDD6E7FBF4C1505895FA445AF4F')
# dev_eui = ubinascii.unhexlify('70B3D5499BD61187')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
counter = 0

while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
    counter += 1
    if counter == 10:
        break

if counter < 10:
    print('Joined')

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
