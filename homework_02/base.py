from abc import ABC
from .exceptions import LowFuelError, NotEnoughFuel, CargoOverload


class Vehicle(ABC):
    def __init__(self, weight=None, started=False, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, new_weight):
        self.weight = new_weight

    @property
    def fuel(self):
        return self.fuel

    @fuel.setter
    def fuel(self, new_fuel):
        self.fuel = new_fuel

    @property
    def fuel_consumption(self):
        return self.fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_fuel_consumption):
        self.fuel_consumption = new_fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise NotEnoughFuel("not enough fuel!")
        else:
            pass

    def move(self):
        pass

