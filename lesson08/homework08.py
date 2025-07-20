# -*- coding: utf-8 -*-
"""
Created on: 30.06.25 19:00
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_dev_courses
@file: homework08.py
"""

"""
Task 1
A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print 'My favorite movie is named {name}'.
"""


def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}")


favorite_movie("Рембо Перша кров")

"""
Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country(name, capital):
    country = {"назва": name, "столиця": capital}
    print(country)


# Приклад використання
make_country("Україна", "Київ")

"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42  
"""

def make_operation(operator, *numbers):
    """
    Здійснює арифметичну операцію («+», «-» або «*»)
    над довільною кількістю числових аргументів.
    """
    if operator not in ('+', '-', '*'):
        raise ValueError("operator має бути лише '+', '-' або '*'")

    if not numbers:
        raise ValueError("потрібно передати принаймні одне число")

    # Додаємо
    if operator == '+':
        result = 0
        for n in numbers:
            result += n
        return result

    # Віднімаємо (починаємо з першого числа, щоб дотриматись порядку)
    if operator == '-':
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result

    # Множимо
    result = 1
    for n in numbers:
        result *= n
    return result

