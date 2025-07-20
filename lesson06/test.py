# -*- coding: utf-8 -*-
"""
Created on: 18.06.25 14:54
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d_nikolaenko
@project name: Python3_dev_courses
@file: test.py
"""

#Який з наступних операторів рівносильний змінній str_c?

str_c = [1, 3].extend([9, 27])
print(str_c)

str_c1 = [1, 3] + [9, 27]
print(str_c1)

#Яка послідовність відповідає наступній послідовності?

a = ('four', ) * 4
print(a)

#Яка довжина наступного кортежу?

a = len(([1, 2, 3], [0, 1], [['чотири'] * 4]))
print(a)
