# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 17:24
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: main.py
"""
import sys
from module2 import run  # Завдання 1
import mymod  # Завдання 3

if __name__ == "__main__":
    print("=== Завдання 1: Імпорт greet з іншого модуля ===")
    run()

    print("\n=== Завдання 2: Робота з sys.path ===")
    import sys_test  # просто викликає демонстрацію

    print("\n=== Завдання 3: Підрахунок рядків і символів ===")
    filename = "test.txt"
    mymod.test(filename)

    # Додатково: можна передати ім'я файлу з командного рядка
    if len(sys.argv) > 1:
        print("\n=== Виклик через аргументи командного рядка ===")
        mymod.test(sys.argv[1])
