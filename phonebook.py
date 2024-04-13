
def menu(phonebook):
    '''Функция организаци меню телефонной книги'''
    while True:
        print('\tPHOHEBOOK\n')
        print('Выберите, что вы хотите сделать?')
        choice = input('1 -> Добавить контакт\n2 -> Посмотреть все контакты\n3 -> Изменить контакт\n4 -> Удалить контакт\n\
5 -> Найти контакт\n6 -> Импортировать данные\n7 -> Выход из программы\n  -> ')
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            show_phonebook(phonebook)
        elif choice == '3':
            print('Извините, раздел находится в разработке\n')
            change_contact(phonebook)
        elif choice == '4':
            print('Извините, раздел находится в разработке\n')
            delete_contact(phonebook)
        elif choice == '5':
            print('Извините, раздел находится в разработке\n')
            find_contact(phonebook)
        elif choice == '6':
            import_data(phonebook)
        elif choice == '7':
            print('Goodbay')
            exit()
        else:
            print('Такой команды не существует!\n')
            continue

def change_contact(phonebook):
    ...

def delete_contact(phonebook):
    ...

def find_contact(phonebook):
    ...
        
def add_contact(phonebook):
    '''Функция создания нового контакта'''
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    list_contact = [last_name, first_name, phone_number] 
    info = ' '.join(list_contact)
    with open(phonebook, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    print('Номер записан!\n')

def show_phonebook(phonebook):
    '''Функция выводящая все контакты'''
    table=[['Last_name', 'First_name', 'Phone_number']]
    with open(phonebook, 'r', encoding='utf-8') as f:
        for line in f:
            table.append(line.split())
        for row in table:
            print('| {:<12} | {:<12} | {:<15} |'.format(*row))
 
def import_data(phonebook):
    '''Функция копирования телефонной книги в другой файл'''
    file_to_add = input('Введите название файла куда копировать телефонную книгу\n')
    with open(file_to_add, 'a', encoding='utf-8') as new_contacts, open(phonebook, 'r', encoding='utf-8') as file:
        for line in file:
            new_contacts.write(line)
        print('Файл успешно создан!')

import os
os.system('cls' if os.name == 'nt' else 'clear')
phonebook = 'phonebook.txt'
menu(phonebook)
