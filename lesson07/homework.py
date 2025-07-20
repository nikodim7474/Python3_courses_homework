# -*- coding: utf-8 -*-
"""
Created on: 18.06.25 14:36
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d_nikolaenko
@project name: Python3_dev_courses
@file: homework1.py
"""

"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values. 

Task 2
Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Compute the total price of the stock where the total price is the sum of the price of
an item multiplied by the quantity of this exact item.

The code has to return the dictionary with the sums of the prices by the goods types.
"""
# Ввід речення з клавіатури
sentence = input("Введіть речення: ")

# Перетворення речення у список слів у нижньому регістрі
words = sentence.lower().split()

# Створюємо порожній словник для підрахунку унікальних слів
word_count = {}

# Проходимо по кожному слову зі списку
for word in words:
    word = word.strip(".,!?\"'")
    if word:
        word_count[word] = word_count.get(word, 0) + 1

# Виводимо результат підрахунку унікальних слів
print("\n Унікальні слова та кількість їх вживань:")
print(word_count)

# Словник із кількістю товарів на складі
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# Словник із цінами за одиницю кожного товару
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

inventory_value = {}

# Обчислюємо сумарну вартість кожного товару як: кількість * ціна
for item in stock:
    inventory_value[item] = stock[item] * prices.get(item, 0)

# Виводимо словник із загальною вартістю кожного типу товару
print("\n💰 Загальна вартість за типами товарів:")
print(inventory_value)

"""
Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and
'j' is corresponding to 'i' squared.
"""

my_list = [(i, i**2) for i in range(1, 11)]
print(my_list)

"""
Task 4
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
"""

# Створення списку днів тижня (англійською мовою)
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Список днів тижня: {days_of_week}")

# Створення словника {номер: "День"} в один рядок
# Використовуємо dict comprehension з enumerate, щоб почати нумерацію з 1
number_to_day = {i + 1: day for i, day in enumerate(days_of_week)}
print(f"Словник {number_to_day}: {number_to_day}") # Змінено 'num_to_day' на 'number_to_day' для відповідності змінній

# Створення зворотного словника {"День": номер} в один рядок
# Використовуємо dict comprehension для обміну ключів і значень
day_to_number = {day: num for num, day in number_to_day.items()}
print(f"Зворотний словник {day_to_number}: {day_to_number}") # Змінено 'day_to_num' на 'day_to_number' для відповідності змінній

# Приклад використання словників:
print(f"\nДень з номером 3: {number_to_day[3]}")
print(f"Номер дня 'Saturday': {day_to_number['Saturday']}") # Змінено 'Субота' на 'Saturday'
