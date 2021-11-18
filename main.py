# Data is sent to Pybytes. Needs to flashed with Pybyte firmware
import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom
import struct

# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    temp = result.temperature
    humidity = result.humidity

    print('Temp:', temp, 'Humidity:', humidity)

    """
    Prepare the data by packing it before sending it to sigfox
    Payload format is: >bb BB HHHH HHHH HHHH where
    b = Temperature         (1 byte,  8 bits,  signed)       Range: -128 to 127
    B = Humidity            (1 byte,  8 bits,  unsigned)     Range: 0 to 255
    H = Pressure            (2 bytes, 16 bits, unsigned)     Range: 0 to 65,535
    H = Air Quality         (2 bytes, 16 bits, unsigned)     Range: 0 to 65,535
    """
    package = struct.pack('>bB',
                            int(temp),
                            int(humidity))
    s.send(package)

    time.sleep(60)
