# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 17:37
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: homework02.py
"""

"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which catches an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).  
"""

def calculate_division():
    try:
        # Отримуємо введення від користувача
        a = float(input("Введіть перше число (a): "))
        b = float(input("Введіть друге число (b): "))

        # Обчислюємо результат
        result = (a ** 2) / b
        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: Введені значення мають бути числами!")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе!")
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")


# Викликаємо функцію
calculate_division()
