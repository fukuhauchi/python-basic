"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def set_engine(self, instance: Engine):
        super().__init__()

    def start(self):
        pass

    def move(self):
        pass