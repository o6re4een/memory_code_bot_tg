import telebot
from telebot import types
from questions import question
import apiyandex
import os
from dotenv import load_dotenv
from platform_request import authorize_user
load_dotenv()

TOKEN = os.getenv('TOKEN')
kioku_bot = telebot.TeleBot(TOKEN)

quest = 0
answs = []
@kioku_bot.message_handler(commands=['start'])
def greeting(message):
    info = 'Введите ваш логин и пароль через пробел'

    msg = kioku_bot.send_message(message.chat.id, info)
    kioku_bot.register_next_step_handler(msg, log_in)


@kioku_bot.message_handler(content_types=['text'])


def log_in(message):
    try:
        log_in_arr = []
        log_in_arr.append(message.text.split(' ')[0])
        log_in_arr.append(message.text.split(' ')[1])
        access_token = authorize_user(log_in_arr[0], log_in_arr[1])
        
        info = 'Введите любой символ для начала анкетирования'
        msg = kioku_bot.send_message(message.chat.id, info)
        kioku_bot.register_next_step_handler(msg, answers)
    except Exception as e:
        msg = kioku_bot.send_message(message.chat.id, 'Данные для входа неверные!\nВведите заново!')
        kioku_bot.register_next_step_handler(msg, log_in)


def answers(message):
    global quest
    global answs
    
    if quest < len(question):
        text = question[quest]
        
        msg = kioku_bot.send_message(message.chat.id, text)
        kioku_bot.register_next_step_handler(msg, answers)

        answs.append(message.text)
        print(answs)

        quest += 1
    else:

        answs.append(message.text)

        quest = 0
        global answs_end
        answs_end = answs
        describtion = apiyandex.get_biography(answs_end)
        print(describtion)
        epitafy = describtion['result']['alternatives'][0]['message']['text']
        kioku_bot.send_message(message.chat.id, epitafy + '\n' + 'Введите любой символ для повторения анкетирования')

        answs = []


kioku_bot.infinity_polling()