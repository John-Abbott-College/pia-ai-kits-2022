import os
import argparse
import time
from datetime import datetime
import pyaudio
import wave
from pixels import Pixels
import subprocess
from dataclasses import dataclass


# Defaults
FILE_NAME_BASE = "room_audio"
NUMBER_OF_SAMPLES = 100
SLEEP_SECS = 5
DATA_FOLDER = "samples/"
ACTIVITY_LABEL = "activity"
NO_ACTIVITY_LABEL = "empty"

RECORD_SECONDS = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 0  # refer to input device id
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2
CHUNK = 1024
SAMPLE_FLUSH_SECS = 0.5  # time to remove from beginning of sample


def config_arguments():

    # Prepare parser for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--empty', action='store_true',
                        help="add 'empty' label to sample")
    parser.add_argument('-a', '--activity', action='store_true',
                        help="add 'activity' label to sample")
    parser.add_argument('-n', '--number_samples', type=int, default=NUMBER_OF_SAMPLES,
                        help=f"Number of samples to take in a row, defaults to {NUMBER_OF_SAMPLES}")
    parser.add_argument('-s', '--sleep', type=int, default=SLEEP_SECS,
                        help=f"time internal between samples in seconds, defaults to {SLEEP_SECS}")
    parser.add_argument('-l', '--length', type=int, default=RECORD_SECONDS,
                        help=f"total sample time length in seconds, defaults to {RECORD_SECONDS}")
    parser.add_argument('-f', '--filename', type=str, default=FILE_NAME_BASE,
                        help=f"base filename for audio file, defaults to {FILE_NAME_BASE}")
    parser.add_argument('-d', '--directory', type=str, default=DATA_FOLDER,
                        help=f"directory to store csv files. defaults to {DATA_FOLDER}")
    parser.add_argument('-p', '--pixels', action='store_true',
                        help=f"Whether to use pixel lights while running.")
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

    return f"./{args.directory}{data_label}.{time_label}_{args.filename}.wav"


def record_audio(file_name: str, args):
    p = pyaudio.PyAudio()

    stream = p.open(
        rate=RESPEAKER_RATE,
        format=p.get_format_from_width(RESPEAKER_WIDTH),
        channels=RESPEAKER_CHANNELS,
        input=True,
        input_device_index=RESPEAKER_INDEX,)

    print("* recording")

    frames = list()

    for i in range(0, int(RESPEAKER_RATE / CHUNK * (args.length + SAMPLE_FLUSH_SECS))):
        data = stream.read(CHUNK)

        # Beginning of sample consistently included a "pop" sound
        # Number of chunks to remove from beginning of sample
        if i < (int(RESPEAKER_RATE / CHUNK * SAMPLE_FLUSH_SECS)):
            continue
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # creates directory if it does not exists.
    dir = os.path.dirname(file_name)
    if not os.path.exists(dir):
        os.makedirs(dir)

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_sample_size(
        p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


@dataclass
class PixelWrapper:
    enable: bool
    pixels = Pixels()

    def think(self):
        if self.enable:
            self.pixels.think()

    def speak(self):
        if self.enable:
            self.pixels.speak()

    def wakeup(self):
        if self.enable:
            self.pixels.wakeup()

    def off(self):
        if self.enable:
            self.pixels.off()


if __name__ == "__main__":
    args = config_arguments()
    pixels = PixelWrapper(enable=args.pixels)

    pixels.wakeup()

    for i in range(args.number_samples):
        try:
            pixels.think()

            file_name = build_file_name(args)
            record_audio(file_name, args)

            pixels.speak()
            # Don't sleep after taking the last sample
            if i == args.number_samples-1:
                break
            print(f"Waiting {args.sleep} seconds to next recording.")
            time.sleep(args.sleep)

        except KeyboardInterrupt:
            break
        except OSError:
            continue

    pixels.wakeup()
    print("Uploading samples to Edge Impulse")
    output = subprocess.run(
        ["edge-impulse-uploader", f"{args.directory}/*.wav"], capture_output=True, check=True, text=True)
    print(output.stdout)

    pixels.off()
