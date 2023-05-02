# First, install the dependencies via:
#    $ pip3 install requests

import json
import time, hmac, hashlib
import requests
import re, uuid
import seeed_python_reterminal.core as rt
import random
import csv
from grove.grove_loudness_sensor import GroveLoudnessSensor

# Your API & HMAC keys can be found here (go to your project > Dashboard > Keys to find this)
HMAC_KEY = "5c44bd5f4e14a1eb3501e9a6b6953024"
API_KEY = "ei_d4e672796787826c5b52e2fbf8a63f850a83bc6c417e5e85577a29198a25d329"

# empty signature (all zeros). HS256 gives 32 byte signature, and we encode in hex, so we need 64 characters here
emptySignature = ''.join(['0'] * 64)

# use MAC address of network interface as deviceId
device_name =":".join(re.findall('..', '%012x' % uuid.getnode()))

# here we have new data every 16 ms
INTERVAL_MS = 16

if INTERVAL_MS <= 0:
    raise Exception("Interval in miliseconds cannot be equal or lower than 0.")

# here we'll collect 2 seconds of data at a frequency defined by interval_ms
freq =1000/INTERVAL_MS
values_list=[]


f = open('./data.csv', 'w')
writer = csv.writer(f)

writer.writerow(['timestamp','temperature', 'light level'])

# Variable below is for adding timestamps.
i = INTERVAL_MS
START_TIME = time.time()
while True: 
    if time.time() > START_TIME + 10:
        break
# This range
# for i in range (10*int(round(freq,0))):
    # values_list.append(
        # Adding light and temperature sensor data here:
    writer.writerow([i, random.uniform(24, 26), rt.illuminance])
    i*=2
    # )

f.close()
# data = {
#     "protected": {
#         "ver": "v1",
#         "alg": "HS256",
#         "iat": time.time() # epoch time, seconds since 1970
#     },
#     "signature": emptySignature,
#     "payload": {
#         "device_name":  device_name,
#         "device_type": "LINUX_TEST",
#         "interval_ms": 10*int(round(freq,0)),
#         "sensors": [
#             { "name": "temperature", "units": "celsius" },
#             { "name": "light", "units": "lux" },
#         ],
#         "values": values_list
#     }
# }



# # encode in JSON
# encoded = json.dumps(data)

# # sign message
# signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg = encoded.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

# # set the signature again in the message, and encode again
# data['signature'] = signature
# encoded = json.dumps(data)

# # and upload the file
# res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
#                     data=encoded,
#                     headers={
#                         'Content-Type': 'application/json',
#                         'x-file-name': 'temperature-and-light-sensor',
#                         'x-api-key': API_KEY,
#                         'x-label': 'Possible-Activity'
#                     })
# if (res.status_code == 200):
#     print('Uploaded file to Edge Impulse', res.status_code, res.content)
# else:
#     print('Failed to upload file to Edge Impulse', res.status_code, res.content)