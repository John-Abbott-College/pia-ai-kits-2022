# Test script for Seeed Grove Adjustable PIO Motion Sensor
# https://wiki.seeedstudio.com/Grove-Adjustable_PIR_Motion_Sensor

# Turn SENS potentiometer all the way counter-clockwise (least sensitive)
# Turn ONTIME potentiometer all the way clockwise (shortest hold time)

from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor as PIR
import time

def main():
    
    pir = PIR(16)

    def callback():
        print(f'Motion detected.')

    pir.on_detect = callback

    while True:
        print(f'PIR state: {pir.read()}')
        time.sleep(1)

if __name__ == '__main__':
    main()