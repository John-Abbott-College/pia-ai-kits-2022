# Light wrapper for sensors collecting sample data

from abc import ABC, abstractmethod
import seeed_python_reterminal.core as reTerminal
from grove.adc import ADC


class Sensor(ABC):
    """Sensor interface
    """
    @abstractmethod
    def read(self):
        pass


class LightSensor(Sensor):
    def __init__(self) -> None:
        self.sensor = reTerminal

    def read(self):
        return self.sensor.illuminance


class LoudnessSensor(Sensor):
    def __init__(self, adc_channel: int, i2c_address: int = 0x04) -> None:
        self.sensor = ADC(address=i2c_address)
        self.channel = adc_channel

    def read(self):
        return self.sensor.read(self.channel)


class Sampler:
    def __init__(self, *sensor_list) -> None:
        self.sensor_list = (
            # Include sensors here
            LightSensor(),
            LoudnessSensor(adc_channel=0)
        )

    def read_sensors(self) -> list:
        return [sensor.read() for sensor in self.sensor_list]


if __name__ == '__main__':
    sampler = Sampler()
    print(sampler.read_sensors())
