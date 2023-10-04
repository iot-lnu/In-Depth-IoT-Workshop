### 1. Create an account on Datacake 

Create a Datacake account [here](https://app.datacake.de/login). 

### 2. Integration to TheThingsNetwork 
In order to visualize the data sent from our DHT11 sensor that is connected to our *Lopy4* on Datacake, we need to create an `Integration` from the things network to Datacake. Let's go ahead and do that. Click on `Applications` and then navigate to `Integrations` and then `Webhooks` to create a webhook. 

![Alt text](/images/i21.png)

Then click on `+ Add Webhook` and select `Datacake`. 

![Alt text](/images/i22.png)

You will be asked to provide a `Webhook ID` and a `Token`. The `Webhook ID` can be anything you want it to be, as long as it is unique among the other webhook IDs. The `Token` is available in Datacake and you can get it by navigating to your `Profile` -> `Account Settings` -> `API Token` -> `Copy`, as shown in the image below.  

![Alt text](/images/i23.png)

Paste the Token in the Token-field and and click on `Create Datacake Webhook`. You should now see your webhook listed under Webhooks. 

![Alt text](/images/i24.png)

Now that we have created a communication link between The Things Network and Datacake, we can go ahead and create a dashboard. To do that, we first need to create a device (a profile of the sending device). To do that, navigate to `Devices` in the left menu and then click on `+ Add Device`. 

![Alt text](/images/i25.png)

Choose `LoRaWAN` and click on `Next`. 

![Alt text](/images/i26.png)

Select `New Product`, type a `Product Name` (can be anything), and click on `Next`. 

![Alt text](/images/i27.png)

Next, select `The Things Stack V3` and click on `Next`. 

![Alt text](/images/i28.png)

Now, we are asked to provide the DevEUI of the device we want to add, so we paste that. Our `DevEUI` can be found either in the `boot.py` file or in TheThingsNetwork under the device page.

![Alt text](/images/i29.png)

Finally, select the `Free` plan and click on `Add 1 device`. 

![Alt text](/images/i30.png)

Now, if we navigate to `Debug`, we should see some entries already. 

![Alt text](/images/i31.png)

With data flowing into Datacake, we can now go ahead and create a dashboard. First, we need to define two fields. One field is for our temperature value, and the second is for our humidity value. This is done under `Configuration` -> `Fields`.

![Alt text](/images/i32.png)

Select *Integer* as the `Type` of the first field, call it `temperature`, and click on `Add field`. Do the same for humidity and call the field accordingly. 

![Alt text](/images/i33.png)

Once that is done, your fields list show looks something like the following: 

![Alt text](/images/i34.png)

To connect these two fields with the two values that we are sending, we need to have a decoder that assigns these fields with the incoming values. This is done under the `Payload Decoder` section and the decoder should look something like this: 

```js
function Decoder(payload, port) {
    if(port === 1 || port === 2) {
        return [
          {
              field: "TEMPERATURE",
              value: payload[0]
          },
          {
              field: "HUMIDITY",
              value: payload[1]
          }
        ];
    }
}
```

Copy and paste it in the `Payload Decoder` field and click `Save`. Wait around 30 seconds and refresh the page. Your fields should now be populated with the sensor values. 

![Alt text](/images/i35.png)

And finally, we can create our dashboard. To do that, click on `Dashboard`, then toggle the dashboard and click on `+ Add Widget`. 

![Alt text](/images/i36.png)

Choose the `Value` widget and 

![Alt text](/images/i37.png)

Give it a name, then navigate to the `Data` tab and select the `field` you're creating this widget for. Give it a unit and click save. 

![Alt text](/images/i38.png)

You should now see the widget appear. Go ahead and do the same for the humidity value and save the dashboard by toggling it on the right (see the arrow in the image below). 

![Alt text](/images/i39.png)

Play around with the widgets until you're happy with your dashboard. When you're done, you can generate a public link to the dashboard and share it. 

![Alt text](/images/i40.png)

You can do many more things in Datacake, e.g. set thresholds for values and create alarms and notifications for deviating values. 