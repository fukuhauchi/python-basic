from abc import ABC
from .exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, max_cargo=0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("low fuel!")
        else:
            pass

    def move(self):
        if self.fuel >= self.fuel_consumption:
            self.fuel -= self.fuel_consumption
        else:
            raise NotEnoughFuel("not enough fuel!")