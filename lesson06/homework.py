# -*- coding: utf-8 -*-
"""
Created on: 11.06.2025 19:03
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: ndn74
@project name: Python3_dev_courses
@file: homework1.py
"""

"""
Task 1
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""
import random

# Генеруємо список з 10 випадкових чисел від 1 до 100
numbers = []
while len(numbers) < 10:
    numbers.append(random.randint(1, 100))

# Ініціалізуємо змінну для збереження максимального числа
i = 0
max_num = numbers[0]

# Знаходимо найбільше число у списку
while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1

print("Task 1")
print("Список випадкових чисел:", numbers)
print("Найбільше число у списку:", max_num)

"""
Task 2

Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""

# Створення першого списку довжиною 10 з випадковими числами від 1 до 10
list1 = []
while len(list1) < 10:
    list1.append(random.randint(1, 10))

# Створення другого списку довжиною 10 з випадковими числами від 1 до 10
list2 = []
while len(list2) < 10:
    list2.append(random.randint(1, 10))

# Створення третього списку, який містить спільні елементи без дублікатів
common_list  = []
i = 0
while i < len(list1):
    number = list1[i]
    if number in list2 and number not in common_list:
        common_list.append(number)
    i += 1

print("\nTask 2")
print("Перший список:", list1)
print("Другий список:", list2)
print("Спільні елементи:", common_list)

