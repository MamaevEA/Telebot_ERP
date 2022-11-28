# Старт, стартовое меню, добавить запись, удалить запись. Евгений.
# Редактировать запись. Андрей.
# Вывести отчет по параметру. Илья.

import telebot
import json
import random

API_TOKEN='5925350659:AAHpjfR8i-gah2l02XABQTsMSpDfBt2sSSU'

bot = telebot.TeleBot(API_TOKEN)

calc = False
data = {}
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

@bot.message_handler(commands=['start'])
def start_message(message):
    global data
    with open('data.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/Команды', '/Справочник')
        bot.send_message(message.chat.id, 'Привет! Что будем делать с телефонным справочником?', reply_markup=keyboard)
    
@bot.message_handler(commands=['Команды'])
def comands_message(message):
    bot.send_message(message.chat.id,'Чтобы добавить новый контакт, введите команду: \n \
        /Добавить, Ф.И.О. через пробел и номер телефона \n \
            (/Добавить Иванов Иван Иванович 89601234567)')
    bot.send_message(message.chat.id,'Чтобы удалить контакт, введите команду: \n \
        /Удалить и через ID контакта  \n \
            (/Удалить 3474373417)')
    bot.send_message(message.chat.id,'Чтобы найти контакт, введите команду: \n \
        /Найти и ID контакта через пробел \n \
            (/Найти 3474373417)')
        
@bot.message_handler(commands=['Справочник'])
def comands_message(message):
    global data
    with open('data.json', 'rb') as json_file:
        data = json_file.read()
    bot.send_message(message.chat.id, data)

@bot.message_handler(content_types='text')
def check_message(message):
    global calc
    if '/Добавить' in message.text:
        bot.send_message(message.chat.id,'Добавили!')
        msg = message.text
        msg = msg.split(' ')
        name = [msg[1], msg[2], msg[3]]
        name = ' '.join(name)
        unique_sequence = uniqueid()
        ID = next(unique_sequence)
        with open('data.json', encoding='utf-8') as json_file:
            data = {}
            data = json.load(json_file)
        data[ID] = {
            'Name': name,
            'Phone': msg[4]
        }
        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)
    elif '/Удалить' in message.text:
        bot.send_message(message.chat.id,'Удалили!')
        msg = message.text
        msg = msg.split(' ')
        with open('data.json', encoding='utf-8') as json_file:
            data = {}
            data = json.load(json_file) 
        data.pop(msg[1], None)
        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)
    elif '/Найти' in message.text:
        bot.send_message(message.chat.id,'Результат поиска:')
        msg = message.text
        msg = msg.split(' ')
        msg = msg[1]
        print(msg)
        with open('data.json', encoding='utf-8') as json_file:
            data = {}
            data = json.load(json_file)
            search = data[msg]
        bot.send_message(message.chat.id, str(search))

bot.polling()