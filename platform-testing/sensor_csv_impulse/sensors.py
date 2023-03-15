# Light wrapper for sensors collecting data

from abc import ABC, abstractmethod
import seeed_python_reterminal.core as reTerminal
from grove.adc import ADC
from gpiozero import DigitalInputDevice


class Sensor(ABC):
    """Sensor interface
    """
    @abstractmethod
    def read(self):
        pass


class LightSensor(Sensor):
    def __init__(self) -> None:
        pass
        # self.sensor = reTerminal._Core

    def read(self):
        return reTerminal.illuminance  # type: ignore


class LoudnessSensor(Sensor):
    def __init__(self, adc_channel: int, i2c_address: int = 0x04) -> None:
        self.sensor = ADC(address=0x04)
        self.channel = adc_channel

    def read(self):
        return self.sensor.read(self.channel)


class MotionSensor(Sensor):
    def __init__(self, gpio: int) -> None:
        self.sensor = DigitalInputDevice(pin=gpio,)

    def read(self):
        return self.sensor.value
