
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.runner import ImpulseRunner
import io
from data_sampler import Sampler
from sensors import LightSensor, MotionSensor, LoudnessSensor

runner = None

def signal_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def help():
    print('python classify.py <path_to_model.eim>')

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

    if len(args) != 1:
        help()
        sys.exit(2)

    model = args[0]

    #The commented code below is for handling csv files. 

    # features_file = io.open(args[1], 'r', encoding='utf8')
    # features = features_file.read()
    # features = features.strip().split("\n")
    
    # # Strips the header of csv file
    # if isinstance(features[0][0], str):
    #     features.pop(0)

    # i = 0
    # while i < len(features):
    #     features[i] = features[i].split(",")
    #     features[i] = [int(j) for j in features[i][1:]]
    #     i+=1


    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    print('MODEL: ' + modelfile)

    sampler = Sampler(
        LightSensor(),
        MotionSensor(16),
        LoudnessSensor(adc_channel=0)
    )
    runner = ImpulseRunner(modelfile)
    try:
        model_info = runner.init()
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')

        while True:
            res = runner.classify(sampler.read_sensors())
            print("classification:")
            print(res["result"])
            print("timing:")
            print(res["timing"])

    finally:
        if (runner):
            runner.stop()

if __name__ == '__main__':
    main(sys.argv[1:])