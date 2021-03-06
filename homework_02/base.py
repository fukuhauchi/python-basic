from abc import ABC
from .exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("low fuel!")
        else:
            pass

    def move(self, required_distance):
        max_distance = self.fuel // self.fuel_consumption
        if 0 < self.fuel_consumption <= self.fuel and required_distance <= max_distance:
            self.fuel -= required_distance * self.fuel_consumption
        else:
            raise NotEnoughFuel("not enough fuel!")
