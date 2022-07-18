"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, weight=0, started=False, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption, max_cargo)
        self.cargo = cargo

    def load_cargo(self, loaded_cargo):
        if (loaded_cargo + self.cargo) <= self.max_cargo:
            self.cargo += loaded_cargo
        else:
            raise CargoOverload("overload!")

    def remove_all_cargo(self):
        before_removal = self.cargo
        self.cargo -= self.cargo
        return before_removal
