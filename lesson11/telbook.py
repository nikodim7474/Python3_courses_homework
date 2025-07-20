# -*- coding: utf-8 -*-
"""
Created on: 23.06.25 19:24
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_dev_courses
@file: telbook.py
"""

"""
Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
 
The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits, all data should
be saved to loaded JSON.
"""

import json
import sys
import os


class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Помилка: Файл {self.filename} містить некоректний JSON. Створюється пуста телефонна книга.")
                return []
            except Exception as e:
                print(f"Помилка завантаження файлу {self.filename}: {e}. Створюється пуста телефонна книга.")
                return []
        else:
            print(f"Файл {self.filename} не знайдено. Буде створено новий файл після виходу.")
            return []

    def _save_contacts(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.contacts, f, indent=4, ensure_ascii=False)
            print("Дані успішно збережено.")
        except Exception as e:
            print(f"Помилка збереження даних: {e}")

    def add_entry(self):
        first_name = input("Введіть ім'я: ").strip()
        last_name = input("Введіть прізвище: ").strip()
        full_name = f"{first_name} {last_name}".strip()
        phone_number = input("Введіть номер телефону: ").strip()
        city_state = input("Введіть місто або штат: ").strip()

        # Перевірка на дублювання номера телефону
        if any(contact['phone_number'] == phone_number for contact in self.contacts):
            print("Запис з таким номером телефону вже існує.")
            return

        new_entry = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "phone_number": phone_number,
            "city_state": city_state
        }
        self.contacts.append(new_entry)
        print("Запис успішно додано.")

    def _search(self, query, field):
        results = [contact for contact in self.contacts if query.lower() in contact.get(field, '').lower()]
        return results

    def search_by_name(self):
        name = input("Введіть ім'я для пошуку: ").strip()
        results = self._search(name, 'first_name')
        self._display_results(results, "Записи за ім'ям")

    def search_by_last_name(self):
        last_name = input("Введіть прізвище для пошуку: ").strip()
        results = self._search(last_name, 'last_name')
        self._display_results(results, "Записи за прізвищем")

    def search_by_full_name(self):
        full_name = input("Введіть повне ім'я для пошуку: ").strip()
        results = self._search(full_name, 'full_name')
        self._display_results(results, "Записи за повним ім'ям")

    def search_by_phone_number(self):
        phone_number = input("Введіть номер телефону для пошуку: ").strip()
        results = self._search(phone_number, 'phone_number')
        self._display_results(results, "Записи за номером телефону")

    def search_by_city_state(self):
        city_state = input("Введіть місто або штат для пошуку: ").strip()
        results = self._search(city_state, 'city_state')
        self._display_results(results, "Записи за містом/штатом")

    def _display_results(self, results, title):
        if results:
            print(f"\n--- {title} ---")
            for i, contact in enumerate(results, 1):
                print(
                    f"{i}. Ім'я: {contact.get('first_name')}, Прізвище: {contact.get('last_name')}, Повне ім'я: {contact.get('full_name')}, Телефон: {contact.get('phone_number')}, Місто/Штат: {contact.get('city_state')}")
            print("--------------------\n")
        else:
            print("Записів не знайдено.")

    def delete_entry(self):
        phone_number_to_delete = input("Введіть номер телефону запису, який потрібно видалити: ").strip()
        initial_len = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact['phone_number'] != phone_number_to_delete]
        if len(self.contacts) < initial_len:
            print("Запис успішно видалено.")
        else:
            print("Запис з таким номером телефону не знайдено.")

    def update_entry(self):
        phone_number_to_update = input("Введіть номер телефону запису, який потрібно оновити: ").strip()
        found = False
        for contact in self.contacts:
            if contact['phone_number'] == phone_number_to_update:
                print("\nЗнайдено запис для оновлення:")
                print(f"Ім'я: {contact.get('first_name')}")
                print(f"Прізвище: {contact.get('last_name')}")
                print(f"Повне ім'я: {contact.get('full_name')}")
                print(f"Телефон: {contact.get('phone_number')}")
                print(f"Місто/Штат: {contact.get('city_state')}")

                contact['first_name'] = input(
                    f"Нове ім'я (залиште пустим, щоб не змінювати: {contact.get('first_name')}): ").strip() or contact[
                                            'first_name']
                contact['last_name'] = input(
                    f"Нове прізвище (залиште пустим, щоб не змінювати: {contact.get('last_name')}): ").strip() or \
                                       contact['last_name']
                contact['full_name'] = f"{contact['first_name']} {contact['last_name']}".strip()
                contact['phone_number'] = input(
                    f"Новий номер телефону (залиште пустим, щоб не змінювати: {contact.get('phone_number')}): ").strip() or \
                                          contact['phone_number']
                contact['city_state'] = input(
                    f"Нове місто або штат (залиште пустим, щоб не змінювати: {contact.get('city_state')}): ").strip() or \
                                        contact['city_state']

                print("Запис успішно оновлено.")
                found = True
                break
        if not found:
            print("Запис з таким номером телефону не знайдено.")

    def run(self):
        while True:
            print("\n--- Меню Телефонної книги ---")
            print("1. Додати новий запис")
            print("2. Пошук за ім'ям")
            print("3. Пошук за прізвищем")
            print("4. Пошук за повним ім'ям")
            print("5. Пошук за номером телефону")
            print("6. Пошук за містом або штатом")
            print("7. Видалити запис")
            print("8. Оновити запис")
            print("9. Вийти")

            choice = input("Виберіть опцію: ").strip()

            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.search_by_name()
            elif choice == '3':
                self.search_by_last_name()
            elif choice == '4':
                self.search_by_full_name()
            elif choice == '5':
                self.search_by_phone_number()
            elif choice == '6':
                self.search_by_city_state()
            elif choice == '7':
                self.delete_entry()
            elif choice == '8':
                self.update_entry()
            elif choice == '9':
                self._save_contacts()
                print("Дякуємо за використання Телефонної книги!")
                break
            else:
                print("Некоректний вибір. Будь ласка, спробуйте ще раз.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python phone_book.py <назва_файлу.json>")
        sys.exit(1)

    json_filename = sys.argv[1]
    phone_book = PhoneBook(json_filename)
    phone_book.run()
