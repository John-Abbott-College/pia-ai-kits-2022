#!/bin/bash

num_of_samples_to_generate=$1
length_of_sample=$2
# Check for default arguments
if [ $# -eq 0 ]
  then
    num_of_samples_to_generate=10
    length_of_sample=10
fi

# Limiting both arguments to integers.
re='^[[:digit:]]+$'
if ! [[ $num_of_samples_to_generate =~ $re ]] ; then
   echo "error: argument 1 is not an integer" >&2; exit 1
fi

re='^[0-9]+$'
if ! [[ $length_of_sample =~ $re ]] ; then
   echo "error: argument 2 is not a integer" >&2; exit 1
fi

echo "Creating csv file..."
for i in $(seq 1 $num_of_samples_to_generate)
do
    python ./data_to_csv.py -l $length_of_sample
done

echo "Uploading csv files..."
edge-impulse-uploader ./samples/*.csv