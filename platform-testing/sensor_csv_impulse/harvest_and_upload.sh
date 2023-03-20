#!/bin/bash

echo "Creating csv file..."
for i in $(seq 1 10)
do
    python ./data_to_csv.py -l 10
done

echo "Uploading csv files..."
edge-impulse-uploader ./samples/*.csv