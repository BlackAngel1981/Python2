phone_book = []

def open_phone_book():
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        phone_book = data.readlines()
        print('фаил открыт')
        return phone_book


def save_phone_book():
    with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
        for i in phone_book:
           data.write(i)

def show_phone_book():
    print(phone_book)
    if len(phone_book) == 0:
        print('Вы не открыли фаил либо фаил пуст')
    else:
            for i in phone_book:
                print(' '.join(i.split(';')))


def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли фаил либо фаил пуст')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append('\n' + user_info)


def change_phone_book():
    user_info = input('Введите номенр контакта, которого вы хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новый номер контакта: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)

def searh_phone_book():
    user_info = input('Введите номер контакта, которого вы хотите найти: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])

def delete_phone_book():
    user_info = input('Введите номер контакта, которого вы хотите удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            # question = input('Действительно удалить контакт? у - да, n - нет: ')
            # if question == 'y':
            phone_book.pop(i)
            break


phone_book = open_phone_book()


# def choose_action(phonebook):
#     while True:
#         print('Что вы хотите сделать?')
#         user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
# 4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
#         print()
#         if user_choice == '1':
#             file_to_add = input('Введите название импортируемого файла: ')
#             import_data(file_to_add, phonebook)
#         elif user_choice == '2':
#             contact_list = read_file_to_dict(phonebook)
#             find_number(contact_list)
#         elif user_choice == '3':
#             add_phone_number(phonebook)
#         elif user_choice == '4':
#             change_phone_number(phonebook)
#         elif user_choice == '5':
#             delete_contact(phonebook)
#         elif user_choice == '6':
#             show_phonebook(phonebook)
#         elif user_choice == '0':
#             print('До свидания!')
#             break
#         else:
#             print('Неправильно выбрана команда!')
#             print()
#             continue
#
#
# def import_data(file_to_add, phonebook):
#     try:
#         with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
#             contacts_to_add = new_contacts.readlines()
#             file.writelines(contacts_to_add)
#     except FileNotFoundError:
#         print(f'{file_to_add} не найден')
#
#
# def read_file_to_dict(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     headers = ['Фамилия', 'Имя', 'Номер телефона']
#     contact_list = []
#     for line in lines:
#         line = line.strip().split()
#         contact_list.append(dict(zip(headers, line)))
#     return contact_list
#
#
# def read_file_to_list(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contact_list = []
#         for line in file.readlines():
#             contact_list.append(line.split())
#     return contact_list
#
#
# def search_parameters():
#     print('По какому полю выполнить поиск?')
#     search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
#     print()
#     search_value = None
#     if search_field == '1':
#         search_value = input('Введите фамилию для поиска: ')
#         print()
#     elif search_field == '2':
#         search_value = input('Введите имя для поиска: ')
#         print()
#     elif search_field == '3':
#         search_value = input('Введите номер для поиска: ')
#         print()
#     return search_field, search_value
#
#
# def find_number(contact_list):
#     search_field, search_value = search_parameters()
#     search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
#     found_contacts = []
#     for contact in contact_list:
#         if contact[search_value_dict[search_field]] == search_value:
#             found_contacts.append(contact)
#     if len(found_contacts) == 0:
#         print('Контакт не найден!')
#     else:
#         print_contacts(found_contacts)
#     print()
#
#
# def get_new_number():
#     last_name = input('Введите фамилию: ')
#     first_name = input('Введите имя: ')
#     phone_number = input('Введите номер телефона: ')
#     return last_name, first_name, phone_number
#
#
# def add_phone_number(file_name):
#     info = ' '.join(get_new_number())
#     with open(file_name, 'a', encoding='utf-8') as file:
#         file.write(f'{info}\n')
#
#
# def show_phonebook(file_name):
#     list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
#     print_contacts(list_of_contacts)
#     print()
#     return list_of_contacts
#
#
# def search_to_modify(contact_list: list):
#     search_field, search_value = search_parameters()
#     search_result = []
#     for contact in contact_list:
#         if contact[int(search_field) - 1] == search_value:
#             search_result.append(contact)
#     if len(search_result) == 1:
#         return search_result[0]
#     elif len(search_result) > 1:
#         print('Найдено несколько контактов')
#         for i in range(len(search_result)):
#             print(f'{i + 1} - {search_result[i]}')
#         num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
#         return search_result[num_count - 1]
#     else:
#         print('Контакт не найден')
#     print()
#
#
# def change_phone_number(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     print('Какое поле вы хотите изменить?')
#     field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
#     if field == '1':
#         number_to_change[0] = input('Введите фамилию: ')
#     elif field == '2':
#         number_to_change[1] = input('Введите имя: ')
#     elif field == '3':
#         number_to_change[2] = input('Введите номер телефона: ')
#     contact_list.append(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)
#
#
# def delete_contact(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)
#
#
# def print_contacts(contact_list: list):
#     for contact in contact_list:
#         for key, value in contact.items():
#             print(f'{key}: {value:12}', end='')
#         print()
#
#
# if __name__ == '__main__':
#     file = 'Phonebook.txt'
#     choose_action(file)
