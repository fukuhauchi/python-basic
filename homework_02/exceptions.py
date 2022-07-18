"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

__all__ = (
    'LowFuelError',
    'NotEnoughFuel',
    'CargoOverload'
)


class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
