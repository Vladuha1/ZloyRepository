import json

def add():
    print(" ")
    name = input("Введите имя: ")
    phones = input("Введите телефоны через пробел: ").split(" ")
    birthday = input("Введите дату рождения: ")
    email = input("Введите email: ")
    contact = {'phones': phones,
                        'birthday': birthday, 'email': email}
    phonebook[name] = contact
    print(contact)
    print("Контакт добавлен")
    print()