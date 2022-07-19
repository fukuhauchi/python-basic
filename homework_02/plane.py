"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, loaded_cargo):
        if (loaded_cargo + self.cargo) <= self.max_cargo:
            self.cargo += loaded_cargo
        else:
            raise CargoOverload("overload!")

    def remove_all_cargo(self):
        before_removal = self.cargo
        self.cargo -= self.cargo
        return before_removal
