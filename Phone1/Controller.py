import Model
import View


# PYTHON 3.10  метод запустить главное меню
def main_menu():
    while True: # цикличность меню
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Найти контакт')
        print('5. Вернуть полный список')
        print('8. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
    #    ПИТОН 3.10!!! вызывает методы - действия со справочником
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 4:
                search_contact()
            case 5:
                View.printPhoneBook()
            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break 
            # выход из программы

# метод для запуска программы
def start():
    open_file()
    View.printPhoneBook()
    main_menu()


# метод открытие файла  и заполнение массива данными
def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        # строка файла - элемент массива
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        # добавляем  новую строчку Phonebook
        data.write(('\n'.join(Model.phonebook)))


# Метод инпутим и клеим строку
def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

# метод элемент для удаление
def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))
# МЕТОД ПОП! выдергивает элемент из строки и писваивает его контакту + разсплитить по ;
# чтобы контакт стал списком 
    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    # работаем с выдернутым ПОПом по индексу 
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    # суем его обратно!!! склеив на ;
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()


def search_contact():
    print (' ')
    searchStr = str(input('Введите данные для поиска: '))
    print (' ')
    for i in range (len(Model.phonebook)):
        if Model.phonebook[i].find(searchStr) != -1:
            Model.searchArr.append(Model.phonebook[i])
    if len (Model.searchArr) != 0:
        View.printSearch()
    else:
        print ("Запись не найдена")
    Model.searchArr = []

        


  

