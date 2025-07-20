# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 22:52:15 2025

@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: ndn74

"""
# env
name = 'Dmytro'
day = 'Saturday'
s = 'Good day {}! {} is a perfect day to learn some python.'

# The greeting program.
print (f'Good day {name}! {day} is a perfect day to learn some python.')

print (s.format(name,day))

print ('Good day {0}! {1} is a perfect day to learn some python.'.format(name,day))

print ('Good day %s! %s is a perfect day to learn some python.' % (name,day))


# Save your first and last name as separate variables,
# then use string concatenation to add them together with a white 
# space in between and print a greeting.

# env
name = 'Dmytro'
last_name = 'Nikolaenko'
greeting_str = 'Greetings dear'
greeting_str1 = greeting_str + ' ' + name + ' ' + last_name

print('\n')
print('Greetings dear' + '',name + '', last_name)

print(greeting_str + '', name + '', last_name)

print(greeting_str1)

# Using python as a calculator.
#
# Make a program with 2 numbers saved in separate variables a and b,
# then print the result for each of the following: 
#
# - Addition
# - Subtraction
# - Division
# - Multiplication
# - Exponent (Power)
# - Modulus
# - Floor division

# env
a = 21
b = 31

print('\n')
print('Python calculator:')
print('='*18)
print ('Addition\t\t', str(a) + ' +', str(b) + ' = ' + str(a+b))
print ('Subtraction \t {} - {} = '.format(b, a) + str(b-a))
print ('Subtraction \t {} - {} = '.format(a, b) + str(a-b))
print ('Division \t\t {} / {} = '.format(b, a) + str(round(b/a,3)))
print ('Multiplication \t {} * {} = '.format(a, b) + str(a*b))
print ('Exponent \t\t {} ^ {} = '.format(a, b) + str(a**b))
print ('Modulus \t\t {} || {} = '.format(a, b) + str(a%b))
print ('Modulus \t\t {} // {} = '.format(b, a) + str(b//a))
