import telebot
from telebot import types
from questions import question
import apiyandex
import os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv('TOKEN')
kioku_bot = telebot.TeleBot(TOKEN)

quest = 0
answs = []
@kioku_bot.message_handler(commands=['start'])
def greeting(message):
    info = 'Введите ваш логин'
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kioku_bot.send_message(message.chat.id, info)


@kioku_bot.message_handler(content_types=['text'])

def answers(message):
    global quest
    global answs

    if quest < len(question):
        text = question[quest]
        kioku_bot.send_message(message.chat.id, text)
        answs.append(message.text)
        print(answs)

        quest += 1
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('123'))

        kioku_bot.send_message(message.chat.id, 'Конец')
        answs.append(message.text)
        print(answs)

        quest = 0
        global answs_end
        answs_end = answs
        apiyandex.get_biography(answs_end)
        answs = []

kioku_bot.infinity_polling()