# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 17:23
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: sys_test.py
"""
import sys
import os

print("=== Початковий sys.path ===")
print(sys.path)

# Додаємо новий шлях
new_path = os.path.expanduser("~/my_modules")
sys.path.append(new_path)

print("\n=== Після додавання нового шляху ===")
print(sys.path)

print("\nТепер Python буде шукати модулі і в цьому каталозі.")
