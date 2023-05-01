# Edge Impulse Sensor Lab
The files in this folder are a project to create samples that can be uploaded to Edge Impulse, and then run a fully trained model to identify whether or not human activity is occuring in a room using sensor data.

**What is required:**
- An Edge Impulse account and an Edge Impulse project.
- A ReTerminal Raspberry Pi, base hat, sensors and ribbon connector. Philips Screwdriver is reccomended.
- Install [Python Library for reTerminal](https://pypi.org/project/seeed-python-reterminal/)
- If using the [Grove Base Hat](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/) as an ADC (analog to digital converter), install the [Python library for Seeedstudio Grove Devices](https://github.com/Seeed-Studio/grove.py).

- The Edge-Impulse Linux is required as well. Installation [instructions for the Raspberry Pi  can be found here](https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-cpu-gpu-targets/raspberry-pi-4).
	- The installation instructions for Edge Impulse CLI seems to be outdated. Please follow the guide below:
		- https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation
	
- The Edge-Impulse python sdk is required, tutorial to install can be found here: https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/linux-python-sdk


**Note:**
The sensors that are used in this project are the built-in ReTerminal light sensor, [Grove - PIR Motion Sensor](https://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/), and [Grove - Loudness Sensor](https://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/)


## ReTerminal Setup
- Connect the Base Hat to the 40-Pin Raspberry Pi Compatible Header.
  ![Connected Pins](./Assets/Pins.jpg)
- Connect a motion sensor to the PWM Port on the Base Hat.
- Connect a Loudness sensor to the A0 Port on the Base Hat.
![Base Hat Image](./Assets/BaseHat.jpg)

## Remotely Connecting to ReTerminal via SSH
Make sure that both the ReTerminal and your computer are on the same network (wifi or ethernet). If the ReTerminal is the only raspberry pi on the network, you can connect with the code below:
```bash
ssh username@hostname
```
where username is the username of the account on the pi.

If you don't know the host name of your raspberry, you can also connect  using its ip address found by hovering over the network button:


![wifi location](./Assets/wifi.png)

The ip address can also be found by typing:
```bash
ip addr
``` 

The ReTerminal can then be connected by typing:
```bash
ssh username@ipaddress
```
where ipaddress is the ip address of the ReTerminal.

## Creating an Edge Impulse Account

An Edge Impulse account is required to create a model and automatically upload data.

## Cloning Project Repository

To have access to the code used to collect data, it is necessary to clone this repository.

Choose a directory in your computer such as Downloads:

```sh
cd ~/Downloads
```

and then clone this repository:

```sh
git clone https://github.com/John-Abbott-College/pia-ai-kits-2022.git
```

Then navigate to the folder containing the project files:

```sh
cd ./pia-ai-kits-2022/platform-testing/sensor_csv_impulse/
```

## Installing the Edge Impulse tools and dependencies: 
Once you have navigated to the sensor_csv_impulse folder, run the project-prep.sh like below:
```sh
bash project-prep.sh
```
This will install all the packages needed to run this project.

During installation, you should be prompted for your Edge Impulse Account credentials.

After that, you can pick an Edge Impulse project and the installation should be complete.


### harvest_and_upload.sh
You can collect and upload data by running this bash file (assuming that the sensors are properly connected).


```bash
bash ./harvest_and_upload.sh < label >
```

The label must be specified as either "-p" for possible human activity or "-n" for no human activity.

This will generate 10 samples that are 10 seconds in length each in a folder caled "./samples"

You can change change the amount of samples and the length of each individual sample like so:
```bash
bash ./harvest_and_upload.sh < label > < number of samples to generate > < length of seconds >
```
Both arguments would have to be specified if you want to adjust either of them.

**Note:**
The edge-impulse-uploader can be invoked to upload many csv files at once.
```bash
edge-impulse-uploader < file path to csv folder >/*.csv
```
Make sure that the csv files follow the edge-impulse convention described here:
https://docs.edgeimpulse.com/reference/data-ingestion/importing-csv-data

## Training the model
After the data is collected and uploaded to Edge Impulse: the model can then be trained using the Edge Impulse interface.

Help for model training on Edge Impulse can be found here: https://docs.edgeimpulse.com/docs

You can then download the model binary file by executing the code below:
```bash
edge-impulse-runner --download < insert name here >.eim
```

## classify.py
After acquiring the model, you can then run the classify.py script.

Remember to specify a path like so:
```bash
python ./classify.py < path to model >.eim
```
and to make sure that the sensors are properly connected to the ReTerminal.


