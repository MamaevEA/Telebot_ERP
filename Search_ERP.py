# Search and Report module for SQL Database by Ilia Kozlov

import easygui
from easygui import *
from tabulate import tabulate
import tkinter
from tkinter import *
from tkinter import scrolledtext
import json

with open('ERP/data.json', 'r', encoding='utf-8') as input_data:
    data = {}
    data = json.load(input_data)

list1 = [] # List which will contain MAIN keys of the dictionary (i.e. employees IDs)

for var in data.keys():
    list1.append(var)

def phones_list(phones_list, phones_dict): # Print phone numbers list
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['ФИО', 'Должность', 'Подразделение', 'Телефон']]
    for i in range(len(phones_list)):
        inner_list1.append(phones_dict[phones_list[i]]['Name'])
        inner_list1.append(phones_dict[phones_list[i]]['Job_title'])
        inner_list1.append(phones_dict[phones_list[i]]['Subdivision'])
        inner_list1.append(phones_dict[phones_list[i]]['Phone'])
    def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
    k = 1
    while k <= len(inner_list1) + 1:
        cut_list(inner_list2, inner_list1, inner_list3)
        inner_list3.append(inner_list2)
        inner_list2 = []
        k += 1
    return inner_list3
def print_names(print_list, print_dict): # Print all employees
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['Таб. №', 'ФИО', 'Должность', 'Подразделение']]
    for i in range(len(print_list)):
        inner_list1.append(print_list[i])
        inner_list1.append(print_dict[print_list[i]]['Name'])
        inner_list1.append(print_dict[print_list[i]]['Job_title'])
        inner_list1.append(print_dict[print_list[i]]['Subdivision'])
    def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
    k = 1
    while k <= len(inner_list1) + 1:
        cut_list(inner_list2, inner_list1, inner_list3)
        inner_list3.append(inner_list2)
        inner_list2 = []
        k += 1
    return inner_list3
    
def prof_search(prof_list, prof_dict, prof_name): # Print certain positions (aka professions)
    int_count = 0
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['Таб. №', 'ФИО', 'Подразделение']]
    for i in range(len(prof_list)):
        if prof_dict[prof_list[i]]['Job_title'] == prof_name:
            inner_list1.append(prof_list[i])
            inner_list1.append(prof_dict[prof_list[i]]['Name'])
            inner_list1.append(prof_dict[prof_list[i]]['Subdivision']) 
        else:
            int_count += 1
    if int_count == len(prof_list):
        return inner_list2
    else:
        def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
        k = 1
        while k <= len(inner_list1) + 1:
                cut_list(inner_list2, inner_list1, inner_list3)
                inner_list3.append(inner_list2)
                inner_list2 = []
                k += 1
        return inner_list3

def birth_year(birth_list, birth_dict, birth_year): # Print certain birth years
    int_count = 0
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['Таб.№', 'ФИО', 'Должность','Подразделение']]
    for i in range(len(birth_list)):
        if birth_dict[birth_list[i]]['Day of Birth'][2] == birth_year:
            inner_list1.append(birth_list[i])
            inner_list1.append(birth_dict[birth_list[i]]['Name'])
            inner_list1.append(birth_dict[birth_list[i]]['Job_title'])
            inner_list1.append(birth_dict[birth_list[i]]['Subdivision'])
        else:
            int_count += 1
    if int_count == len(birth_list):
        return inner_list2
    else:
        def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
        k = 1
        while k < len(inner_list1):
                cut_list(inner_list2, inner_list1, inner_list3)
                inner_list3.append(inner_list2)
                inner_list2 = []
                k += 1
        return inner_list3

def salary_range(sal_list, sal_dict, s_min, s_max): # Print certain salary range
    int_count = 0
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['Таб. №', 'ФИО', 'Должность', 'Подразделение']]
    for i in range(len(sal_list)):
        if int(sal_dict[sal_list[i]]['Salary']) in range(s_min - 1, s_max + 1):
            inner_list1.append(sal_list[i])
            inner_list1.append(sal_dict[sal_list[i]]['Name'])
            inner_list1.append(sal_dict[sal_list[i]]['Job_title'])
            inner_list1.append(sal_dict[sal_list[i]]['Subdivision'])
        else:
            int_count += 1
    if int_count == len(sal_list):
        return inner_list2
    else:
        def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
        k = 1
        while k <= len(inner_list1) + 1:
                cut_list(inner_list2, inner_list1, inner_list3)
                inner_list3.append(inner_list2)
                inner_list2 = []
                k += 1
        return inner_list3  

def search_menu():
    global choise1
    choise1 = '' # Action received from User
    while choise1 != 'Выйти':
        choises1 = ['Вывод на экран всех сотрудников', 'Телефонный справочник', 'Параметры поиска', 'Выйти']
        msg = 'Выберите Ваш запрос'
        choise1 = (buttonbox(msg, 'Выбор действия', choises1)) # Command received from User
        if choise1 == 'Вывод на экран всех сотрудников':
            all_list = print_names(list1, data)
            def show_widget(list):
                widget1 = Tk()
                widget1.title('Список всех сотрудников')
                widget1.geometry('600x200')
                txt = scrolledtext.ScrolledText(widget1, width=90, height=20)
                txt.grid(column=1, row=1)
                table1 = tabulate(list, headers='firstrow', tablefmt='fancy_grid', stralign='center')
                txt.insert(INSERT, table1)
                mainloop()
            show_widget(all_list)
        elif choise1 == 'Телефонный справочник':
            ph_list = phones_list(list1, data)
            def show_widget(list):
                widget1 = Tk()
                widget1.title('Телефонный справочник')
                widget1.geometry('600x200')
                txt = scrolledtext.ScrolledText(widget1, width=90, height=20)
                txt.grid(column=1, row=1)
                table1 = tabulate(list, headers='firstrow', tablefmt='fancy_grid', stralign='center')
                txt.insert(INSERT, table1)
                mainloop()
            show_widget(ph_list)
        elif choise1 == 'Параметры поиска':
            choise2 = '' # Type of research
            while choise2 != 'Выйти':
                msg2 = 'Выберите тип поиска'
                choises2 = ['Поиск по должности', 'Поиск по году рождения', 'Поиск по диапазону ЗП', 'Выйти']
                choise2 = (buttonbox(msg2, 'Выбор типа поиска', choises2))
                if choise2 == 'Поиск по должности':
                    def input_position():
                        global var_pos
                        input_values1 = enterbox('Введите название должности:')
                        var_pos = str(input_values1)
                        return var_pos
                    def show_widget(list):
                            widget1 = Tk()
                            widget1.title(f'Сотрудники с должностью "{position}"')
                            widget1.geometry('463x200')
                            txt = scrolledtext.ScrolledText(widget1, width=90, height=20)
                            txt.grid(column=1, row=1)
                            table1 = tabulate(list, headers='firstrow', tablefmt='fancy_grid', stralign='center')
                            txt.insert(INSERT, table1)
                            mainloop()
                    position = input_position()
                    position_list = prof_search(list1, data, position)
                    if len(position_list) != 0:
                        show_widget(position_list)
                        while True: # If User wants to check another position
                                if ccbox('Хотите продолжить посик?', 'Выберите следующий шаг'):
                                    position = input_position()
                                    position_list = prof_search(list1, data, position)
                                    if len(position_list) != 0:
                                        show_widget(position_list)
                                    else:
                                        msgbox(f'По запросу "{position}" ничего не найдено. Измените параметры поиска')
                                else:
                                    break
                    else:
                        msgbox(f'По запросу "{position}" ничего не найдено. Измените параметры поиска.')
                        while True: # If User wants to check another position
                                if ccbox('Хотите продолжить посик?', 'Выберите следующий шаг'):
                                    position = input_position()
                                    position_list = prof_search(list1, data, position)
                                    if len(position_list) != 0:
                                        show_widget(position_list)
                                    else:
                                        msgbox(f'По запросу "{position}" ничего не найдено. Измените параметры поиска.')
                                else:
                                    break
                elif choise2 == 'Поиск по году рождения':
                    def input_year():
                        global var_year
                        input_values1 = enterbox('Введите год рождения:')
                        var_year = int(input_values1)
                        return var_year
                    def show_widget(list):
                            widget1 = Tk()
                            widget1.title(f'Сотрудники, родившиеся в {year} году')
                            widget1.geometry('563x200')
                            txt = scrolledtext.ScrolledText(widget1, width=90, height=20)
                            txt.grid(column=1, row=1)
                            table1 = tabulate(list, headers='firstrow', tablefmt='fancy_grid', stralign='center')
                            txt.insert(INSERT, table1)
                            mainloop()
                    year = input_year()
                    year_list = birth_year(list1, data, year)
                    if len(year_list) != 0:
                        show_widget(year_list)
                        while True: # If User wants to check another year
                                if ccbox('Хотите продолжить поиск?', 'Выберите следующий шаг'):
                                    year = input_year()
                                    year_list = birth_year(list1, data, year)
                                    if len(year_list) != 0:
                                        show_widget(year_list)
                                    else:
                                        msgbox(f'Сотрудники {year} года рождения не найдены. Измените параметры поиска.')
                                else:
                                    break
                    else:
                        msgbox(f'Сотрудники {year} года рождения не найдены. Измените параметры поиска.')
                        while True: # If User wants to check another year
                                if ccbox('Хотите продолжить поиск?', 'Выберите следующий шаг'):
                                    year = input_year()
                                    year_list = birth_year(list1, data, year)
                                    if len(year_list) != 0:
                                        show_widget(year_list)
                                    else:
                                        msgbox(f'Сотрудники {year} года рождения не найдены. Измените параметры поиска.')
                                else:
                                    break
                elif choise2 == 'Поиск по диапазону ЗП':
                    def input_salary():
                        global var_min
                        global var_max
                        range_list = ['От', 'До']
                        input_values = []
                        input_values = multenterbox('Введите диапазон ЗП', 'Поиск по диапазону ЗП', range_list)
                        var_min = int(input_values[0])
                        var_max = int(input_values[1])
                    def show_widget(list):
                            widget1 = Tk()
                            widget1.title(f'ЗП в диапазоне от {min} до {max}')
                            widget1.geometry('600x200')
                            txt = scrolledtext.ScrolledText(widget1, width=90, height=20)
                            txt.grid(column=1, row=1)
                            table1 = tabulate(list, headers='firstrow', tablefmt='fancy_grid', stralign='center')
                            txt.insert(INSERT, table1)
                            mainloop()
                    input_salary()
                    min = var_min
                    max = var_max
                    salary_list = salary_range(list1, data, min, max)
                    if len(salary_list) != 0:
                        show_widget(salary_list)
                        while True: # If User wants to check another range
                            if ccbox('Хотите продолжить поиск?', 'Выберите следующий шаг'):
                                input_salary()
                                min = var_min
                                max = var_max
                                salary_list = salary_range(list1, data, min, max)
                                if len(salary_list) != 0:
                                    show_widget(salary_list)
                                else:
                                    msgbox(f'В диапазоне от {min} до {max} рублей ничего не найдено. Измените параметры поиска.')
                            else:
                                break
                    else:
                        msgbox(f'В диапазоне от {min} до {max} рублей ничего не найдено. Измените параметры поиска')
                        while True: # If User wants to check another range
                            if ccbox('Хотите продолжить поиск?', 'Выберите следующий шаг'):
                                input_salary()
                                min = var_min
                                max = var_max
                                salary_list = salary_range(list1, data, min, max)
                                if len(salary_list) != 0:
                                    show_widget(salary_list)
                                else:
                                    msgbox(f'В диапазоне от {min} до {max} рублей ничего не найдено. Измените параметры поиска.')
                            else:
                                break
        elif choise1 == 'Выйти':
            exit()

#search_menu()