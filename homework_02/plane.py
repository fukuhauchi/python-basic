"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        super().__init__()
        self.cargo = cargo
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

    def start(self):
        pass

    def move(self):
        pass