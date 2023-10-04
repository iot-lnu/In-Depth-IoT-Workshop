import pycom
import time
from machine import Pin
from dht import DTH

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue
th = DTH(Pin('P23', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)

while True:
    result = th.read()
    if result.is_valid():
        pycom.rgbled(0x001000) # green
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        # send some data
        s.send(bytes([result.temperature, result.humidity]))
    time.sleep(30)  