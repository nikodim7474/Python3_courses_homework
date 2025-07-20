# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 20:55:08 2025

@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: ndn74

"""

"""
Task 1

String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'
Expected Result : 'held'

Sample String: 'my'
Expected Result : 'mymy'

Sample String: 'x'
Expected Result: Empty String

Tips:
    - Use built-in function len() on an input string
    - Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""
print('Task 1')
# Приклад вхідного рядка
input_string = "helloworld" # Спробуйте змінити цей рядок на інші значення

# Змінна для зберігання результату
result_string = ""

# Перевіряємо довжину рядка
if len(input_string) < 2:
  result_string = ""
else:
  # Отримуємо перші 2 і останні 2 символи та об'єднуємо їх
  result_string = input_string[:2] + input_string[-2:]

# Виводимо результат
print(f"Вхідний рядок: '{input_string}'")
print(f"Отриманий рядок: '{result_string}'")

print("-" * 30) # тут і далі просто для краси та відокремлення результату :)

# Приклад з іншим рядком: "my"
input_string = "my"
if len(input_string) < 2:
  result_string = ""
else:
  result_string = input_string[:2] + input_string[-2:]
print(f"Вхідний рядок: '{input_string}'")
print(f"Отриманий рядок: '{result_string}'")

print("-" * 30) # тут і далі просто для краси та відокремлення результату :)

# Приклад з іншим рядком: "x"
input_string = "x"
if len(input_string) < 2:
  result_string = ""
else:
  result_string = input_string[:2] + input_string[-2:]
print(f"Вхідний рядок: '{input_string}'")
print(f"Отриманий рядок: '{result_string}'")

print("-" * 30) # тут і далі просто для краси та відокремлення результату :)

# Приклад з порожнім рядком: ""
input_string = ""
if len(input_string) < 2:
  result_string = ""
else:
  result_string = input_string[:2] + input_string[-2:]
print(f"Вхідний рядок: '{input_string}'")
print(f"Отриманий рядок: '{result_string}'")

"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

print('\nTask 2')
# Вхідний рядок для перевірки телефонного номера
phone_number_string = "0987654321"

# Змінна для зберігання повідомлення про результат
validation_message = ""

# Перевірка, чи рядок містить тільки цифрові символи
# і чи його довжина дорівнює 10 символам.
if phone_number_string.isdigit() and len(phone_number_string) == 10:
  validation_message = f"Рядок '{phone_number_string}' є дійсним телефонним номером."
else:
  validation_message = f"Рядок '{phone_number_string}' не є дійсним телефонним номером."
  if not phone_number_string.isdigit():
    validation_message += " Він містить нецифрові символи."
  if len(phone_number_string) != 10:
    validation_message += f" Його довжина становить {len(phone_number_string)} символів, а має бути 10."

# Виводимо повідомлення про результат
print(validation_message)

print("-" * 50)  # тут і далі просто для краси та відокремлення результату :)

#Неправильна довжина
phone_number_string = "12345"
validation_message = ""
if phone_number_string.isdigit() and len(phone_number_string) == 10:
  validation_message = f"Рядок '{phone_number_string}' є дійсним телефонним номером."
else:
  validation_message = f"Рядок '{phone_number_string}' не є дійсним телефонним номером."
  if not phone_number_string.isdigit():
    validation_message += " Він містить нецифрові символи."
  if len(phone_number_string) != 10:
    validation_message += f" Його довжина становить {len(phone_number_string)} символів, а має бути 10."
print(validation_message)

print("-" * 50)

# Нецифрові символи
phone_number_string = "Q987654321"
validation_message = ""
if phone_number_string.isdigit() and len(phone_number_string) == 10:
  validation_message = f"Рядок '{phone_number_string}' є дійсним телефонним номером."
else:
  validation_message = f"Рядок '{phone_number_string}' не є дійсним телефонним номером."
  if not phone_number_string.isdigit():
    validation_message += " Він містить нецифрові символи."
  if len(phone_number_string) != 10:
    validation_message += f" Його довжина становить {len(phone_number_string)} символів, а має бути 10."
print(validation_message)

print("-" * 50)

# Порожній рядок
phone_number_string = ""
validation_message = ""
if phone_number_string.isdigit() and len(phone_number_string) == 10:
  validation_message = f"Рядок '{phone_number_string}' є дійсним телефонним номером."
else:
  validation_message = f"Рядок '{phone_number_string}' не є дійсним телефонним номером."
  if not phone_number_string.isdigit():
    validation_message += " Він містить нецифрові символи."
  if len(phone_number_string) != 10:
    validation_message += f" Його довжина становить {len(phone_number_string)} символів, а має бути 10."
print(validation_message)

"""
Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.
"""
print('\nTask 2')
# Визначаємо математичний вираз та правильну відповідь
num1 = 7
num2 = 4
operation = "+"
correct_answer = num1 + num2

# Формуємо рядок для відображення виразу користувачу
expression_string = f"Скільки буде {num1} {operation} {num2}?"

# Запитуємо у користувача відповідь
print(expression_string)
try:
  user_answer_str = input("Введіть вашу відповідь: ")
  user_answer = int(user_answer_str) # Перетворюємо вхідні дані користувача на ціле число

  # Перевіряємо відповідь користувача
  if user_answer == correct_answer:
    print("Правильно! Ваша відповідь вірна.")
  else:
    print(f"Неправильно. Правильна відповідь: {correct_answer}.")
except ValueError:
  # Обробляємо випадок, коли користувач ввів нечислові дані
  print("Невірний ввід. Будь ласка, введіть число.")

print("-" * 50)

# Інший приклад з множенням
num1 = 12
num2 = 5
operation = "*"
correct_answer = num1 * num2
expression_string = f"Скільки буде {num1} {operation} {num2}?"

print(expression_string)
try:
  user_answer_str = input("Введіть вашу відповідь: ")
  user_answer = int(user_answer_str)

  if user_answer == correct_answer:
    print("Правильно! Ваша відповідь вірна.")
  else:
    print(f"Неправильно. Правильна відповідь: {correct_answer}.")
except ValueError:
  print("Невірний ввід. Будь ласка, введіть число.")

"""
Task 4

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""
print('\nTask 2')
# Змінна, в якій зберігається ім'я (малими літерами)
stored_name = "антон"

# Запитуємо ім'я у користувача
user_input_name = input("Будь ласка, введіть своє ім'я: ")

# Перетворюємо введене ім'я користувача на малі літери для порівняння без урахування регістру
user_input_name_lower = user_input_name.lower()

# Перевіряємо, чи вхідні дані відповідають збереженому імені
if user_input_name_lower == stored_name:
  print(f"Привіт, {user_input_name}! Ваше ім'я '{user_input_name}' відповідає збереженому імені '{stored_name}'.")
else:
  print(f"Вибачте, {user_input_name}! Ваше ім'я '{user_input_name}' не відповідає збереженому імені '{stored_name}'.")

print("-" * 50)

# Ім'я введено з великої літери
user_input_name = "Антон"
user_input_name_lower = user_input_name.lower()
print(f"Тестуємо з вводом '{user_input_name}'")
if user_input_name_lower == stored_name:
  print(f"Привіт, {user_input_name}! Ваше ім'я '{user_input_name}' відповідає збереженому імені '{stored_name}'.")
else:
  print(f"Вибачте, {user_input_name}! Ваше ім'я '{user_input_name}' не відповідає збереженому імені '{stored_name}'.")

print("-" * 50)

# Ім'я не співпадає
user_input_name = "Марія"
user_input_name_lower = user_input_name.lower()
print(f"Тестуємо з вводом '{user_input_name}'")
if user_input_name_lower == stored_name:
  print(f"Привіт, {user_input_name}! Ваше ім'я '{user_input_name}' відповідає збереженому імені '{stored_name}'.")
else:
  print(f"Вибачте, {user_input_name}! Ваше ім'я '{user_input_name}' не відповідає збереженому імені '{stored_name}'.")
