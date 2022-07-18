"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, engine=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, volume, pistons):
        self.engine = Engine(volume, pistons)
