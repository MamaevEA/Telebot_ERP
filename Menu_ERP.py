import easygui
from easygui import *  
import json
import random
from Search_ERP import search_menu
from tabulate import tabulate
from tkinter import *

def menu(): # Создает интерфейс меню
    global type_vvod        # Переменная, куда записывается выбор пользователя
    type_vvod = ''
    output=''
    while output != "Выйти":        # Пока не будет выбрана кнопка "Выйти", меню будет возобновляться
        msg = "Информационная система управления базой данных сотрудников компании 'Рога и копыта'"
        title = "Меню"
        choices = ["Принять нового сотрудника", "Уволить сотрудника", \
        "Редактировать данные сотрудника", "Вывести отчет", "Выйти"]
        output = buttonbox(msg, title, choices)
        if output == "Принять нового сотрудника":
            type_vvod = 1
            vvod()
            new_people()
        elif output == "Уволить сотрудника":
            type_vvod = 2
            dell()
            del_people()
        elif output == "Редактировать данные сотрудника":
            type_vvod = 3
            edit()
            edit_people()
        elif output == "Вывести отчет":
            search_menu()
        elif output == "Выйти!":
            exit()
    
def vvod(): # Создает интерфейс ввода нового сотрудника
    global var1                 # Переменная куда будем записывать ФИО, Дату рождения, Телефон и Оклад.
    global sex                  # Переменная, куда записывают пол сотрудника.
    global job_title            # Переменная, куда записывают должность сотрудника.
    global subdivision          # Переменная, куда записывают подразделение сотрудника
    msg = "Введите данные сотрудника"   # Сообщение
    title = "Ввод нового сотрудника"    # Шапочка.
    fieldNames = ["Фамилия, Имя, Отчество", "День рождения (дд)", "Месяц рождения (мм)", \
        "Год рождения (гггг)", "Телефон", "Оклад"]
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    var1 = fieldValues      # Запись данных в переменную в виде листа
    
    fieldValues = []            # Следующее окно интерфейса выбора пола
    title = "Выбор пола"
    msg = var1[0]
    fieldNames = ["Мужской", "Женский"] # Сюда можно добавить словарь
    fieldValues = buttonbox(msg,title, fieldNames)
    sex = fieldValues           # Данные о поле записаны в переменную sex

    fieldValues = []            # Следующее окно интерфейса выбора должности
    title = "Выбор должности"
    msg = var1[0]
    fieldNames = ["Директор", "Начальник отдела", "Менеджер по продажам", "Инженер", \
        "Бухгалтер", "Уборщик"] # Сюда можно добавить словарь
    fieldValues = choicebox(msg,title, fieldNames)
    job_title = fieldValues     # Данные о должности записаны в переменную job_title

    fieldValues = []            # Следующее окно интерфейса выбора подразделения
    title = "Выбор подразделения"
    msg = var1[0]
    fieldNames = ["Администрация", "Отдел продаж", "ИТ-отдел", "АХО"] # Сюда можно добавить словарь
    fieldValues = choicebox(msg,title, fieldNames)
    subdivision = fieldValues     # Данные о подразделении записаны в переменную subdivision

def dell():
    global dell_human       # Переменная, куда записывается ID сотрудника, которого надо удалить
    msg = "Введите табельный номер сотрудника, которого хотите удалить из базы данных"   # Сообщение
    title = "Удаление сотрудника"    # Шапочка.
    fieldNames = ["Табельный номер"]  # Ввод ID
    fieldValues = multenterbox(msg,title, fieldNames)
    dell_human = fieldValues[0]      # Запись ID удаляемого сотрудника в переменную dell_human


def edit():             
    global edit_human    # Переменная, куда записывается ID сотрудника, которого надо отредактировать
    msg = "Введите табельный номер сотрудника, данные которого хотите откорректировать"   # Сообщение
    title = "Редактирование данных сотрудника"    # Шапочка.
    fieldNames = ["Табельный номер"]  # Ввод ID
    fieldValues = multenterbox(msg,title, fieldNames)
    edit_human = fieldValues[0]      # Запись ID корректируемого сотрудника в переменную edit_human

def report():
        global type_report
        msg = "По какому признаку вы хотите сформировать отчет?"
        title = "Отчеты"
        choices = ["По должности", "По году рождения", \
        "По диапазону зарплат", "А можно всех посмотреть? ;)"]
        output = buttonbox(msg, title, choices)
        
        if output == "По должности":
            fieldValues = []            # Следующее окно интерфейса выбора должности
            title = "Выбор должности"
            fieldNames = ["Директор", "Начальник отдела", "Менеджер по продажам", "Инженер", \
                    "Бухгалтер", "Уборщик"] # Сюда можно добавить словарь
            fieldValues = choicebox(msg,title, fieldNames)
            type_report = fieldValues     # Данные о должности записаны в переменную type_report
        
        elif output == "По году рождения": # Следующее окно интерфейса ввода года
            title = "Ввод года рождения"    
            fieldNames = ["Год рождения"]  
            fieldValues = []  
            fieldValues = multenterbox(msg,title, fieldNames)
            type_report = fieldValues      # Запись года рождения в переменную type_report
        
        elif output == "По диапазону зарплат": # Следующее окно ввода диапазона зарплат
            title = "Ввод диапазона зарплат"    
            fieldNames = ["Минимум", "Максимум"]  
            fieldValues = []  
            fieldValues = multenterbox(msg,title, fieldNames)
            type_report = fieldValues      # Запись диапазона зарплат в переменную type_report
        elif output == "А можно всех посмотреть? ;)":
            type_report = "All"     
            # При выводе всех сотрудников, в переменную type_report записывается строка "All".

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def new_people():
        unique_sequence = uniqueid()
        ID = next(unique_sequence)
        dob = [int(var1[1]), int(var1[2]), int(var1[3])]
        with open('ERP/data.json', encoding='utf-8') as json_file:
            data = {}
            data = json.load(json_file)
        data[ID] = {
            'Name': var1[0],
            'Sex': sex,
            'Day of Birth': dob,
            'Phone': var1[4],
            'Salary': var1[5],
            'Job_title': job_title,
            'Subdivision': subdivision
        }

        with open('ERP/data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)

def del_people():
    with open('ERP/data.json', encoding='utf-8') as json_file:
        data = {}
        data = json.load(json_file)
        data.pop(dell_human, None)
    with open('ERP/data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

def edit_people():
    with open('ERP/data.json', encoding='utf-8') as json_file:
        data = {}
        data = json.load(json_file)
        msg = data[edit_human]   # Сообщение
        title = "Какие данные будете редактировать?"    # Шапочка. 
        fieldNames = ["Фамилия, Имя, Отчество", "День рождения (дд)", "Месяц рождения (мм)", \
        "Год рождения (гггг)", "Телефон", "Оклад", "Пол", "Должность", "Подразделение"]
        fieldValues = choicebox(msg,title, fieldNames)
        edit_but = fieldValues      # Запись данных в переменную в виде листа 
        if edit_but == "Фамилия, Имя, Отчество":
            msg = "Введите новые ФИО"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Фамилия, Имя, Отчество"]  # Ввод 
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Name"] = edit_but_f
        elif edit_but == "День рождения (дд)":
            msg = "Введите новую дату рождения"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["День рождения (дд)"]  # Ввод 
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Day of Birth"][0]= int(edit_but_f) 
        elif edit_but == "Месяц рождения (мм)":
            msg = "Введите новую дату рождения"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Месяц рождения (мм)"]  # Ввод 
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Day of Birth"][1]= int(edit_but_f) 
        elif edit_but == "Год рождения (гггг)":
            msg = "Введите новую дату рождения"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Год рождения (гггг)"]  # Ввод
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Day of Birth"][2]= int(edit_but_f) 
        elif edit_but == "Телефон":
            msg = "Введите новый телефон"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Телефон"]  # Ввод
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Phone"] = edit_but_f
        elif edit_but == "Оклад":
            msg = "Введите новый оклад"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Оклад"]  # Ввод
            fieldValues = multenterbox(msg,title, fieldNames)
            edit_but_f = fieldValues[0]
            data[edit_human]["Salary"] = edit_but_f
        elif edit_but == "Пол":
            msg = "Введите новый пол"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Мужской", "Женский"] # Сюда можно добавить словарь
            fieldValues = buttonbox(msg,title, fieldNames)
            edit_but_f = fieldValues
        elif edit_but == "Должность":
            msg = "Введите новую должность"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Директор", "Начальник отдела", "Менеджер по продажам", "Инженер", \
                "Бухгалтер", "Уборщик"] # Сюда можно добавить словарь
            fieldValues = choicebox(msg,title, fieldNames)
            edit_but_f = fieldValues
            data[edit_human]["Job_title"] = edit_but_f
        elif edit_but == "Подразделение":
            msg = "Введите новое подразделение"   # Сообщение
            title = "Редактирование данных сотрудника"    # Шапочка.
            fieldNames = ["Администрация", "Отдел продаж", "ИТ-отдел", "АХО"] 
            # Сюда можно добавить словарь
            fieldValues = choicebox(msg,title, fieldNames)
            edit_but_f = fieldValues
            data[edit_human]["Subdivision"] = edit_but_f 
    with open('ERP/data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

    


