# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 17:37
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: homework01.py
"""

""" 
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

def oops():
    # Викликаємо IndexError явно
    raise IndexError("Це явний виклик IndexError")

def catch_error():
    try:
        oops()
    except IndexError:
        print("Перехопили IndexError!")
    except KeyError:
        print("Перехопили KeyError!")
    except:
        print("Перехопили інший виняток!")

# Викликаємо функцію для перевірки
catch_error()

# Якщо змінимо oops на виклик KeyError:
def oops():
    # Тепер викликаємо KeyError
    raise KeyError("Це явний виклик KeyError")

# Викликаємо знову
catch_error()

