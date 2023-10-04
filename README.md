# Basic IoT Workshop 
![image alt](https://lnu.se/api/media/27188-w849h425cy12cw849ch413 "title")

   * [Agenda](#agenda)
   * [Requiered hardware](#requiered-hardware)
   * [Required Software](#required-software)
   * [Conneting the hardware](#conneting-the-hardware)
      * [Lopy and Expansionboard](#lopy-and-expansionboard)
      * [LoRaWAN Antenna](#lorawan-antenna)
      * [DHT11 Sensor](#dht11-sensor)
   * [Create project &amp; Read sensor data](#create-project--read-sensor-data)
   * [Transmitt data using LoRaWAN](#transmitt-data-using-lorawan)
   * [Visualize data using Datacake](#visualize-data-using-datacake)

## Agenda

- Short presentation
- Part 1, Get started with the hardware & Send data
- Break
- Part 2, Send & visualise data

## Requiered hardware

|   Name	            |   Type  	                                |Quantity|  
|   :-:	                |   :-:	                                    |  :-:	 |
|   Lopy4	            |   Development board	                    |   1	 | 
|   Expansion Board V.3	|   Expansion board	                        |   1	 | 
|   Antenna	            |   LoRa (868MHz/915MHz), Sigfox Antenna	|   1	 |  
|   DHT11	            |   Temperature & Humidity sensor	        |   1 	 |   
|   Breadboard	        |   -	                                    |   1	 |   
|   Cables	            |   Jumper wires	                        |   3	 |  
|   USB-cable	        |   Micro USB 	                            |   1	 |

## Required Software
To get started with programming the pycom device, you will need to install the following: 

- [Visual Studio Code](https://code.visualstudio.com/download)
- [NodeJs](https://nodejs.org/en/download/current)
- [Pymakr for VSCode](https://docs.pycom.io/gettingstarted/software/vscode/)

## Conneting the hardware 

### Lopy and Expansionboard
![Alt text](/images/i4.png)

### LoRaWAN Antenna

![Alt text](/images/i1.png)


### DHT11 Sensor
![Alt text](/images/i2.png)

 

## Create project & Read sensor data
This tutorial guides you through creating a Lopy4 project in Visual Studio Code, connecting to the device, importing the necessary sensor library, and writing and syncing code to read temperature and humidity data from a DHT11 sensor.

[Click here](read.md) to continue. 

## Transmitt data using LoRaWAN
This tutorial guides you on how to connect a Lopy4 device to The Things Stack (TTS) platform. The steps involve account creation, application setup, device registration, and code implementation for sending temperature and humidity data via LoRaWAN.

[Click here](send.md) to continue. 

## Visualize data using Datacake
In this tutorial, you learn how to visualize sensor data on a cloud dashboard using Datacake and The Things Network. Steps include setting up an account on both platforms, linking them via a webhook, creating a device on Datacake, defining specific fields for sensor data, creating a payload decoder, and then finally setting up a dashboard with widgets for real-time data visualization.

[Click here](visualize.md) to continue. 