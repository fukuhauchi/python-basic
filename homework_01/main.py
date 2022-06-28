"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return [num ** 2 for num in numbers]
"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = lambda x: x % 2 != 0
EVEN = lambda x: x % 2 == 0
PRIME = "prime"

def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            break
    else:
        if number != 1:
            return number


def filter_numbers(numbers_list, filter_type):
    if filter_type == ODD or filter_type == EVEN:
        return list(filter(filter_type, numbers_list))
    else:
        return list(filter(is_prime, numbers_list))
"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
