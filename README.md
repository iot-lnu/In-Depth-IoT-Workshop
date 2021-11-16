
###### tags: `TA Stuff`

### Table of Contents
[TOC]

# The Things Stack (TTS)

:::danger
**⚠️ Important ⚠️ Make sure the LoRa antenna is connected properly before running any LoRa or Sigfox code on your device. Not doing so might break your device.** You can find how to properly connect the antenna [here](#Connect-the-antenna).
:::

## 1. Register
Before you can start using TTS, you need to [create a TTS account](https://account.thethingsnetwork.org/register). Once you have done that, go ahead and navigate to Console.

![](https://i.imgur.com/eb22wU8.png)

Then select Europe 1 (eu1) and choose the `Login with The Things ID` option to log in.

![](https://i.imgur.com/3apo8Cv.png)


## 2. Create an application
Once you've logged in, you'll be redirected to the your homepage. There, you navigate to `Create an application`.

Give the application an appropriate ID, name and description.

![](https://i.imgur.com/gkJoy8n.png)

When the application is created, you'll be redirected to the application page.

![](https://i.imgur.com/wvWgZf0.png)

## 3. Add the pycom device to the application

Once there, navigate to `Add end device` in the bottom-right corner to add your pycom device to the application. The Lopy4 is not in TTS's LoRaWAN device repository yet, but you can still add it manually.

![](https://i.imgur.com/sCTVvij.png)

Make sure to select `OTAA` as the activation mode and `MAC V1.0.2` as the LoRaWAN version and press `Start`.

More information about activation modes can be found [here](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/).

The next step is to enter your device information. The `DevEUI` can be retrieved from your pycom device by running the following code-snippet in your interpreter, either in Atom or VSCode.

```python=
from network import LoRa
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

The output should look something like:

```python=
70B3D54997C25011
```

This is your `DevEUI` and is a unique identifier for your node/device. Copy that and paste it in the `DevEUI` field, as shown in the image below:

![](https://i.imgur.com/q5haIze.png)

Give your end device an appropriate device ID and fill the `AppEUI` with zeros by pressing on the `00` to the right of the `AppEUI` field. End device name and description are optional, but recommended if you add multiple end devices to your application. When you're done, proceed to the next step by clicking the `Network layer settings` button at the bottom-right corner.

![](https://i.imgur.com/7PKNw6G.png)

Set the frequency plan to `Europe 863-870 MHz (SF9 for RX2 - recommended)` and the regional parameters version to `PHY V1.0.2 REV A`. Once done, proceed to the final step by clicking the `Join settings` button at the bottom-right corner.

In this final step, you generate your `AppKey` and add your end device to your application.

![](https://i.imgur.com/KM0uAQ1.png)


Once you've added your end device to your application, you should be redirected to your device page. The landing page should look like:

![](https://i.imgur.com/LrkMxl3.png)


## 4. Connect to TTS using your pycom device

Now, you connect to TTS using the `AppKey` you generated earlier.

:::danger
**⚠️ Important ⚠️ Make sure the LoRa antenna is connected properly before running any LoRa or Sigfox code on your device. Not doing so might break your device.** You can find how to properly connect the antenna [here](#Connect-the-antenna).
:::

First, add the snippet below at the begining of your `boot.py` that you have in your project folder in Atom or VSCode.

```python=
from network import LoRa
import time
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('00000000000000000000000000000000')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')

# Your old code from main.py should be here

```

:::info
Remove duplicate imports if you have any after adding the snippet above.
:::

Now, replace the zeros in row 8 with your `AppKey`. In our case, the generated `AppKey` was `2AFCC3031C924792687395AB9D384262`. Note that only row 8 is changed.


```python=
from network import LoRa
import time
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('2AFCC3031C924792687395AB9D384262')# Add your own app_key here

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')

# Your old code from main.py should be here

```

Try to run `boot.py` and now in the console, you should see something like:


![](https://i.imgur.com/mvCfxwu.png)

Congratulations, you have now successfully connected to TTS and are ready to start sending messages!

:::warning
If your device tries to join for more than a few minutes, then it is an indication of poor coverage in your area. Perhaps you should consider other networks, like [Helium](https://hackmd.io/ikBVVe3zQymcUxo6rbIdlQ?view) or [Sigfox](https://hackmd.io/iItkcV_XTgCdjRooqlUyOg?view).
:::

## 5. Send messages with TTS

In order to send messages with TTS, you need to import one additional library in your `main.py` file, the `socket` library. Then, you create a socket and configure it and finally use it to send a message with TTS. Below, you can see how your `main.py` file should look like.

```python=
import socket
import time

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)


# Your old code from main.py should be here

# EXAMPLE: Create a DHT object, collect data in the loop and send it

while True:
    temperature = 23    # Mock value
    humidity = 40       # Mock value
    s.send(bytes([temperature, humidity]))
    print('sent temperature:', temperature)
    print('sent humidity:', humidity)
    time.sleep(900)     # wait 900 seconds (15 minutes) before sending again

```

By running the code-snippet above (in Atom or VSCode), you should get an output similar to the one below.

![](https://i.imgur.com/U6ibv2X.png)

And in the end device page in your TTS console, you should see something like:

![](https://i.imgur.com/AxRUix5.png)

The interesting part is the first line, where you can see the type of the data and preview. The MAC-payload in this message matches your bytes-array you sent using the socket you created.

```python=
s.send(bytes([temperature, humidity]))
```

matches

![](https://i.imgur.com/OyALAlz.png)


Note that the MAC payload is in hex (base 16).


:::warning
On The Things Network's public community network a Fair Use Policy applies which limits the uplink airtime to 30 seconds per day (24 hours) per node and the downlink messages to 10 messages per day (24 hours) per node. More about that [here](https://www.thethingsnetwork.org/forum/t/fair-use-policy-explained/1300).
:::
