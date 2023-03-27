# Edge Impulse Sensor Lab
The files in this folder are a project to create samples that can be uploaded to Edge Impulse, and then run a fully trained model to identify whether or not human activity is occuring in a room using sensor data.

**What is required:**
- An Edge Impulse account and an Edge Impulse project.
- A Reterminal Raspberry Pi.
- The Edge-Impulse python sdk is required, tutorial to install can be found here: https://docs.edgeimpulse.com/docs/edge-impulse-for-linux/linux-python-sdk

## harvest_and_upload.sh
You can collect and upload data by running this bash file (assuming that the sensors are properly connected).
```bash
bash ./harvest_and_upload.sh < label >
```
The label must be specified as either "-m" for possible human activity or "-s" for no human activity.

This will generate 10 samples that are 10 seconds in length each in a folder caled "./samples"

You can change change the amount of samples and the length of each individual sample like so:
```bash
bash ./harvest_and_upload.sh < label > < number of samples to generate > < length of seconds >
```
Both arguments would have to be specified if you want to adjust either of them.
## Training the model
After the data is collected and uploaded to Edge Impulse: the model can then be trained using the Edge Impulse interface.

Help for training on Edge Impulse can be found here: https://docs.edgeimpulse.com/docs

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
and to make sure that the sensors are properly connected to the reterminal.


