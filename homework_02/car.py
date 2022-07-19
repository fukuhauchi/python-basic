"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, engine_instance: Engine):
        self.engine = engine_instance
