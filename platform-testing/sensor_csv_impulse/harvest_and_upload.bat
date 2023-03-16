echo "Creating csv file..."
python ./platform-testing/sensor_csv_impulse/data_to_csv.py

echo "Uploading csv files..."
edge-impulse-uploader ./samples/*.csv