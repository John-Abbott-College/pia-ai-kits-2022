import os
from data_sampler import Sampler
from sensors import LightSensor, MotionSensor, LoudnessSensor
import argparse
import time
from datetime import datetime
import csv
import random as r

"""Save collected data to csv file using Edge Impulse format.
"""
# Defaults
FILE_NAME_BASE = "_Human_Activity."
INTERVAL_MS = 1000
SAMPLE_LENGTH_SECS = 5
DATA_FOLDER = "samples/"
POTENTIAL_MOTION_LABEL = "Potential"
NO_MOTION_LABEL = "No"


def config_arguments():

    # Prepare parser for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--no', action='store_true',
                        help="add 'No' label to sample")
    parser.add_argument('-p', '--potential', action='store_true',
                        help="add 'Potential' label to sample")
    parser.add_argument('-i', '--interval', type=int, default=INTERVAL_MS,
                        help="time internal between samples in milliseconds")
    parser.add_argument('-l', '--length', type=int, default=SAMPLE_LENGTH_SECS,
                        help="total sample time length in seconds")
    parser.add_argument('-f', '--filename', type=str, default=FILE_NAME_BASE,
                        help="base filename for csv file")
    parser.add_argument('-d', '--directory', type=str, default=DATA_FOLDER,
                        help="directory to store csv files")
    return parser.parse_args()


def build_file_name(cli_args) -> str:
    """Builds a file name based on CLI arguments

    :return str: File name to be saved with timestamp and sample type
    """
    timestamp = time.time()

    if cli_args.no:
        data_label = NO_MOTION_LABEL
    elif cli_args.potential:
        data_label = POTENTIAL_MOTION_LABEL
    else:
        data_label = ""

    human_time = datetime.fromtimestamp(timestamp)
    time_label = str(human_time).replace(
        " ", "T").split(".")[0].replace(":", "-")

    return f"./{args.directory}{data_label}{args.filename}_{time_label}.csv"


def write_to_csv(file_name: str, data: list[list]):
    #creates directory if it does not exists.
    dir = os.path.dirname(file_name)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('timestamp', 'light level', 'motion detected state', 'loudness' ))
        writer.writerows(data)


def collect_data(sampler: Sampler, interval_ms: int, sample_length: int) -> list[list]:
    """Takes measurements of all sensors according to time interval and sample length

    :param int interval: time interval between readinds in milliseconds
    :param int sample_length: total sample length in seconds
    :return list[list]: list of readings where each reading is a list of data from all sensors
    """
    data = list()
    no_readings = 0

    # helper inner function to calculate ellapsed time.
    def delta_time(previous_time: float) -> float:
        return time.perf_counter() - previous_time

    # time.time() is not guaranteed to be accurate so we'll use it for timestamps and
    # time.perf_counter() for tracking time intervals.
    interval_secs = interval_ms/1000
    data_timestamp = 0 
    start_counter = time.perf_counter()
    current_counter = start_counter

    # Take first reading and prepend with timestamp
    data_row = sampler.read_sensors()
    data_row.insert(0, data_timestamp)
    data.append(data_row)
    no_readings += 1
    current_counter = time.perf_counter()

    while (delta_time(start_counter)) <= sample_length:
        if delta_time(current_counter) < interval_secs:
            pass
        else:
            # Timestamp entries are expected to be in milliseconds.
            data_timestamp += interval_ms
            # reading_start = time.perf_counter() # debugging only
            reading = sampler.read_sensors()
            # Alternate readings in case of sensors not working...
            # reading = [r.randint(0, 20), 0, r.randint(0, 50)]
            # reading = [r.randint(0, 20), 0, r.randint(51, 150)]
            # reading = [r.randint(0, 20), 1, r.randint(0, 50)]
            # reading = [r.randint(0, 20), 1, r.randint(51, 150)]
            # reading = [r.randint(50, 100), 0, r.randint(0, 50)]
            # reading = [r.randint(50, 100), 0, r.randint(51, 150)]
            # reading = [r.randint(50, 100), 1, r.randint(0, 50)]

            # print("reading took", time.perf_counter() - reading_start, "secs") # debugging only
            reading.insert(0, data_timestamp)
            data.append(reading)
            current_counter = time.perf_counter()
            no_readings += 1

    print("final time: ", delta_time(start_counter), "with", no_readings,
          "readings, sample length", sample_length, "secs, reading interval", interval_ms, "ms")
    return data


if __name__ == "__main__":
    args = config_arguments()
    file_name = build_file_name(args)

    sampler = Sampler(
        LightSensor(),    # taking about 0.5 secs for a reading?!
        MotionSensor(16),
        LoudnessSensor(adc_channel=0)
    )

    data = collect_data(sampler, args.interval, args.length)
    print(data)
    write_to_csv(file_name, data)
