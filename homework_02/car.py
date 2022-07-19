"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, input_volume, input_pistons):
        self.engine = Engine(volume=input_volume, pistons=input_pistons)
