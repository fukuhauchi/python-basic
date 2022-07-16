from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=None, started=False, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
