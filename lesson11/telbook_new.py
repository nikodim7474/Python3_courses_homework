# -*- coding: utf-8 -*-
"""
Created on: 21.07.25 18:02
@author: Dmytro Nikolaenko (nikodim74@gmail.com)
@user: d.nikolaenko
@project name: Python3_courses_homework
@file: telbook_new.py
"""

"""
Функціональність додатка «Телефонна книга»:

Додавання нових записів 
Пошук за іменем 
Пошук за прізвищем 
Пошук за повним ім'ям
Пошук за номером телефону
Пошук за містом або штатом
Видалення запису для заданого номера телефону
Оновлення запису для заданого номера телефону
Опція виходу з програми

Першим аргументом програми має бути назва телефонної книги, якщо аргумент пустий то створюється файл noname.json,
після чого повинна завантажити дані JSON, якщо файл пустий топопередити про це. Після виходу користувача всі дані
повинні бути збережені в завантаженому JSON.
"""

import json
import os
from typing import Dict, List, Optional


class PhoneBook:
    def __init__(self, filename: str = "noname.json"):
        self.filename = filename
        self.contacts = self._load_phone_book()

    def _load_phone_book(self) -> List[Dict]:
        """Завантажує телефонну книгу з JSON файлу або створює нову, якщо файл не існує або порожній."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if not data:
                        print("ℹ️ Файл телефонної книги порожній. Почнемо з чистої книги.")
                    return data
            else:
                print(f"ℹ️ Файл '{self.filename}' не знайдено. Створено нову телефонну книгу.")
                return []
        except json.JSONDecodeError:
            print(f"⚠️ Помилка при читанні файлу '{self.filename}'. Створено нову телефонну книгу.")
            return []

    def save_phone_book(self):
        """Зберігає телефонну книгу у JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, ensure_ascii=False, indent=4)

    def add_contact(self):
        """Додає новий контакт до телефонної книги."""
        print("\n" + "➕ ДОДАВАННЯ НОВОГО КОНТАКТУ " + "―" * 20)
        contact = {
            'first_name': input("│ Ім'я: ").strip(),
            'last_name': input("│ Прізвище: ").strip(),
            'full_name': "",
            'phone': input("│ Номер телефону: ").strip(),
            'city': input("│ Місто: ").strip(),
            'state': input("│ Штат/область: ").strip()
        }
        contact['full_name'] = f"{contact['first_name']} {contact['last_name']}"

        # Перевірка на унікальність номеру телефону
        if any(c['phone'] == contact['phone'] for c in self.contacts):
            print(f"⚠️ Помилка: контакт з номером {contact['phone']} вже існує!")
            return

        self.contacts.append(contact)
        print("✅ Контакт успішно доданий!")

    def search_by(self, field: str, value: str) -> List[Dict]:
        """Шукає контакти за вказаним полем."""
        results = []
        for contact in self.contacts:
            if value.lower() in contact.get(field, '').lower():
                results.append(contact)
        return results

    def display_contacts(self, contacts: List[Dict]):
        """Виводить список контактів у читабельному форматі."""
        if not contacts:
            print("\n🔍 Контакти не знайдені")
            return

        print("\n" + "📋 РЕЗУЛЬТАТИ ПОШУКУ " + "―" * 50)
        for i, contact in enumerate(contacts, 1):
            print(f"│ {i}. {contact['full_name']}")
            print(f"│ 📞 Телефон: {contact['phone']}")
            print(f"│ 🏙 Місцезнаходження: {contact['city']}, {contact['state']}")
            print("├" + "―" * 60)

    def delete_contact(self, phone: str):
        """Видаляє контакт за номером телефону."""
        for i, contact in enumerate(self.contacts):
            if contact['phone'] == phone:
                del self.contacts[i]
                print(f"✅ Контакт з номером {phone} видалений!")
                return
        print(f"⚠️ Контакт з номером {phone} не знайдений!")

    def update_contact(self, phone: str):
        """Оновлює контакт за номером телефону."""
        for contact in self.contacts:
            if contact['phone'] == phone:
                print("\n" + "✏️ ОНОВЛЕННЯ КОНТАКТУ " + "―" * 40)
                print("│ (Залиште поле порожнім, щоб не змінювати)\n")

                new_first = input(f"│ Ім'я [{contact['first_name']}]: ").strip()
                new_last = input(f"│ Прізвище [{contact['last_name']}]: ").strip()
                new_phone = input(f"│ Телефон [{contact['phone']}]: ").strip()
                new_city = input(f"│ Місто [{contact['city']}]: ").strip()
                new_state = input(f"│ Штат/область [{contact['state']}]: ").strip()

                if new_first:
                    contact['first_name'] = new_first
                if new_last:
                    contact['last_name'] = new_last
                if new_phone and new_phone != phone:
                    # Перевірка на унікальність нового номеру
                    if any(c['phone'] == new_phone for c in self.contacts):
                        print("⚠️ Помилка: цей номер телефону вже використовується!")
                        return
                    contact['phone'] = new_phone
                if new_city:
                    contact['city'] = new_city
                if new_state:
                    contact['state'] = new_state

                contact['full_name'] = f"{contact['first_name']} {contact['last_name']}"
                print("✅ Контакт успішно оновлений!")
                return

        print(f"⚠️ Контакт з номером {phone} не знайдений!")


def display_menu():
    """Виводить головне меню програми."""
    print("\n" + "=" * 60)
    print("📖 ТЕЛЕФОННА КНИГА".center(60))
    print("=" * 60)
    print("1. Додати новий контакт")
    print("2. Пошук за ім'ям")
    print("3. Пошук за прізвищем")
    print("4. Пошук за повним ім'ям")
    print("5. Пошук за номером телефону")
    print("6. Пошук за містом або штатом")
    print("7. Видалити контакт")
    print("8. Оновити контакт")
    print("9. Вийти з програми")
    print("=" * 60)


def main():
    import sys

    # Визначаємо ім'я файлу телефонної книги
    filename = sys.argv[1] if len(sys.argv) > 1 else "noname.json"
    phone_book = PhoneBook(filename)

    while True:
        display_menu()
        try:
            choice = input("Виберіть опцію (1-9): ").strip()

            if choice == '1':
                phone_book.add_contact()

            elif choice in ['2', '3', '4', '5', '6']:
                fields = {
                    '2': 'first_name',
                    '3': 'last_name',
                    '4': 'full_name',
                    '5': 'phone',
                    '6': 'city'
                }
                field = fields[choice]
                search_prompt = {
                    '2': "ім'я",
                    '3': "прізвище",
                    '4': "повне ім'я",
                    '5': "номер телефону",
                    '6': "місто або штат"
                }[choice]
                value = input(f"Введіть {search_prompt} для пошуку: ").strip()
                results = phone_book.search_by(field, value)
                phone_book.display_contacts(results)

            elif choice == '7':
                phone = input("Введіть номер телефону для видалення: ").strip()
                phone_book.delete_contact(phone)

            elif choice == '8':
                phone = input("Введіть номер телефону для оновлення: ").strip()
                phone_book.update_contact(phone)

            elif choice == '9':
                phone_book.save_phone_book()
                print("\n" + "=" * 60)
                print("📚 Дані збережено. До побачення!".center(60))
                print("=" * 60)
                break

            else:
                print("⚠️ Невірний вибір. Будь ласка, введіть число від 1 до 9.")

        except KeyboardInterrupt:
            print("\n📚 Дані збережено. До побачення!")
            phone_book.save_phone_book()
            break
        except Exception as e:
            print(f"⚠️ Сталася помилка: {e}")


if __name__ == "__main__":
    main()
