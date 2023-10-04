### 1. Register
Before you can start using TTS, you need to [create a TTS account](https://account.thethingsnetwork.org/register). Once you have done that, go ahead and navigate to Console.

![](https://i.imgur.com/eb22wU8.png)

Then select Europe 1 (eu1) and choose the `Login with The Things ID` option to log in.

![](https://i.imgur.com/3apo8Cv.png)


### 2. Create an application
Once you've logged in, you'll be redirected to your homepage. There, you navigate to `Create an application`. 

Give the application an appropriate ID, name, and description. 

![](https://i.imgur.com/gkJoy8n.png)

When the application is created, you'll be redirected to the application page. 

![](https://i.imgur.com/wvWgZf0.png)

### 3. Add the Lopy4 to the application

Once there, navigate to `Register end device` in the bottom-right corner to add your *Lopy4* to the application. The *Lopy4* is not in TTS's LoRaWAN device repository yet, but you can still add it manually.

Set the **frequency plan** to `Europe 863-870 MHz (SF9 for RX2 - recommended)`, **LoRaWAN version** to `MAC V1.0.2` and the **regional parameters version** to `PHY V1.0.2 REV A`. 

Set the `JoinEUI` to **0000000000001234**, generate the `DevEUI` and the `AppKey`, and click on `Register end device`. 

![Alt text](/images/i15.png)

Once you register your device, you will be directed to the device page, which should look similar to the image below. 

![Alt text](/images/i16.png)

Next, we need to add some code that allow us to connect to the network. Add the code below to your `boot.py` and upload the code to the device and run it. Update the `app_eui`, `dev_eui`, and the `app_key` fields to reflect the recently generated ones (in the previous step). You can find those keys under the device page in TheThingsNetwork.

```py
from network import LoRa
import socket
import time
import ubinascii

app_eui = '0000000000001234'
dev_eui = '70B3D57ED00617EA'
app_key = 'A63A0CD9EC46317A2E11B74D93C08E56'


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, and change them to the provided credentials
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

# send some data
s.send(bytes([0x01, 0x02, 0x03]))
```

Once the file is executed, you should see when the device attempts to join the network and when it finally succeeds to join. 

![Alt text](/images/i17.png)

And on The Things Network device `Live data`, we should see output similar to the following: 

![Alt text](/images/i18.png)

In the `Live data` section above, we can see that the payload of the message we sent is 3 bytes, which were `1`, `2`, and `3` (`01 02 03` in hex). Those were just random numbers, but now we need to send the temperature and humidity values that we previously read. So let's modify the code in `main.py` to be as follows: 

```py
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
```

Uploading this code and restarting the *Lopy4* should yield the following output:

![Alt text](/images/i19.png)

And in The Things Network `Live data`, we can read the sensor values in the payload (as hex). We can see 17 (23 in decimal), which is our temperature, followed by 30 (48 in decimal), which is our humidity. 

![Alt text](/images/i20.png)

If you made it this far, congratulations! 🥳 

You can now move on to visualizing the data! 