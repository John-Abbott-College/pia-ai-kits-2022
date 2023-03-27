#!/bin/bash

label=$1
num_of_samples_to_generate=$2
length_of_sample=$3

if [$# -eq 0]
   then
   echo "Error: the label argument must be provided." >&2; exit 1
fi

if  [ $label != "-s" ] && [ $label != "-m"]
   then
   echo "Error: you must provide either an -s (no human activity) or a -m (possible human activity) as the first argument to denote which label the data will be sampled for." >&2; exit 1
fi
# Check for default arguments
if [ $# -eq 1 ]
  then
    num_of_samples_to_generate=10
    length_of_sample=10
fi

# Limiting both arguments to integers.
re='^[[:digit:]]+$'
if ! [[ $num_of_samples_to_generate =~ $re ]] ; then
   echo "Error: argument 1 is not an integer" >&2; exit 1
fi

re='^[0-9]+$'
if ! [[ $length_of_sample =~ $re ]] ; then
   echo "Error: argument 2 is not a integer" >&2; exit 1
fi

echo "Creating csv file..."
for i in $(seq 1 $num_of_samples_to_generate)
do
   python ./data_to_csv.py $label -l $length_of_sample
done

# echo "Uploading csv files..."
# edge-impulse-uploader ./samples/*.csv