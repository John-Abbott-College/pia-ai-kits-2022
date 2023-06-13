import time
from sensors import Sensor


class Sampler:
    """Data sampler class that groups and collects data from all sensors.
    """

    def __init__(self, *sensor_list: Sensor) -> None:
        """Sampler constructor. Receives a list of sensors as arguments
        """
        self.sensors = sensor_list

    def read_sensors(self) -> list:
        """Reads all sensors contained in sampler

        :return list: returns a list of readings using a list comprehension.
        """
        return [sensor.read() for sensor in self.sensors]


if __name__ == '__main__':

    from sensors import LightSensor, MotionSensor, LoudnessSensor

    sampler = Sampler(
        LightSensor(),
        MotionSensor(16),
        LoudnessSensor(adc_channel=0)
    )

    while 1:
        print(sampler.read_sensors())
        time.sleep(2)
