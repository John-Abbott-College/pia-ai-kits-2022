import os
import argparse
import time
from datetime import datetime
import pyaudio
import wave
import numpy as np


"""Save collected data to csv file using Edge Impulse format.
"""
# Defaults
FILE_NAME_BASE = ".room_audio_"
INTERVAL_SECS = 10
SAMPLE_LENGTH_SECS = 5
DATA_FOLDER = "samples/"
ACTIVITY_LABEL = "activity"
NO_ACTIVITY_LABEL = "empty"

RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 0  # refer to input device id
CHUNK = 1024
RECORD_SECONDS = 10
# WAVE_OUTPUT_FILENAME = ".room_audio_.wav"


def config_arguments():

    # Prepare parser for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--empty', action='store_true',
                        help="add 'empty' label to sample")
    parser.add_argument('-a', '--activity', action='store_true',
                        help="add 'activity' label to sample")
    parser.add_argument('-i', '--interval', type=int, default=INTERVAL_SECS,
                        help="time internal between samples in seconds")
    parser.add_argument('-l', '--length', type=int, default=SAMPLE_LENGTH_SECS,
                        help="total sample time length in seconds")
    parser.add_argument('-f', '--filename', type=str, default=FILE_NAME_BASE,
                        help="base filename for audio file")
    parser.add_argument('-d', '--directory', type=str, default=DATA_FOLDER,
                        help="directory to store csv files")
    return parser.parse_args()


def build_file_name(cli_args) -> str:
    """Builds a file name based on CLI arguments

    :return str: File name to be saved with timestamp and sample type
    """
    timestamp = time.time()

    if cli_args.empty:
        data_label = NO_ACTIVITY_LABEL
    elif cli_args.activity:
        data_label = ACTIVITY_LABEL
    else:
        data_label = "unspecified"

    human_time = datetime.fromtimestamp(timestamp)
    time_label = str(human_time).replace(
        " ", "T").split(".")[0].replace(":", "-")

    return f"./{args.directory}{data_label}{args.filename}{time_label}.wav"


def record_audio(file_name: str):
    p = pyaudio.PyAudio()

    stream = p.open(
        rate=RESPEAKER_RATE,
        format=p.get_format_from_width(RESPEAKER_WIDTH),
        channels=RESPEAKER_CHANNELS,
        input=True,
        input_device_index=RESPEAKER_INDEX,)

    print("* recording")

    frames = []

    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        # extract channel 0 data from 2 channels, if you want to extract channel 1, please change to [1::2]
        a = np.fromstring(data, dtype=np.int16)[0::2]
        frames.append(a.tostring())

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(
        p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == "__main__":
    args = config_arguments()
    file_name = build_file_name(args)
    record_audio(file_name)    
