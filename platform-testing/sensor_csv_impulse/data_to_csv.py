from data_sampler import Sampler
from sensors import LightSensor, MotionSensor, LoudnessSensor
import argparse
import time
from datetime import datetime
import csv

"""Save collected data to csv file using Edge Impulse format.
"""

FILE_NAME_BASE = "detect_motion_data"
INTERVAL_MS = 50
SAMPLE_LENGTH_SECS = 10
DATA_FOLDER = "samples/"


def config_arguments():
    # Prepare parser for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--still', action='store_true')
    parser.add_argument('-m', '--motion', action='store_true')
    return parser.parse_args()


def build_file_name(data_folder: str, base_name: str, timestamp: float, cli_args) -> str:
    """Builds a file name based on a timestamp and a sample mode passed as a CLI argument

    :param str base_name: Base name of saved file
    :return str: File name to be saved with timestamp and sample type
    """
    if cli_args.still:
        data_label = "still-"
    elif cli_args.motion:
        data_label = "motion-"
    else:
        data_label = ""

    human_time = datetime.fromtimestamp(timestamp)
    time_label = str(human_time).replace(" ", "T").split(".")[0]

    return f"./{data_folder}{data_label}{base_name}-{time_label}.csv"


def write_to_csv(file_name: str, data: list[list]):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('timestamp', 'temperature', 'light level'))
        writer.writerows(data)


def collect_data(interval: int = 20, sample_length: int = 10):
    data = list()

    #TODO: Collect data according to interval and sample lenght.
    for _ in range(10):
        data.append(sampler.read_sensors())

    return data


if __name__ == "__main__":
    args = config_arguments()
    timestamp = time.time()
    file_name = build_file_name(DATA_FOLDER, FILE_NAME_BASE, timestamp, args)

    sampler = Sampler(
        LightSensor(),
        MotionSensor(16),
        LoudnessSensor(adc_channel=0)
    )

    data = collect_data()
    print(data)
    write_to_csv(file_name, data)
