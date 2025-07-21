# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 17:23
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: mymod.py
"""
def count_lines(name):
    """Повертає кількість рядків у файлі"""
    with open(name, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def count_chars(name):
    """Повертає кількість символів у файлі"""
    with open(name, 'r', encoding='utf-8') as f:
        return len(f.read())

def test(name):
    """Викликає обидві функції й друкує результат"""
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Файл: {name}")
    print(f"Рядків: {lines}")
    print(f"Символів: {chars}")
