# Старт, стартовое меню, добавить запись, удалить запись. Евгений.
# Редактировать запись. Андрей.
# Вывести отчет по параметру. Илья.

import telebot
import json

API_TOKEN='5925350659:AAHpjfR8i-gah2l02XABQTsMSpDfBt2sSSU'

bot = telebot.TeleBot(API_TOKEN)

calc = False
data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    global data
    with open('ERP/data.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Готов к работе!', reply_markup=keyboard) 

@bot.message_handler(commands=['menu'])
def show_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    #eq = message.text.split()[1:]
    #print(eq[0])
    #print(eval(eq[0]))
    calc=True
    bot.send_message(message.chat.id,'А теперь введите выражение для расчета')    

@bot.message_handler(content_types='text')
def check_message(message):
    global calc
    if 'привет' in message.text:
        bot.send_message(message.chat.id,'И тебе привет коли не шутишь!')  
    if calc:
         calc=False
         bot.send_message(message.chat.id,'результат равен '+str(eval(message.text)))


bot.polling()