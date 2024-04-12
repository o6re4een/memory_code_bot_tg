import telebot
from telebot import types
from questions import question
import apiyandex
import os
from dotenv import load_dotenv
from platform_request import authorize_user
from vedis import Vedis
import config
import dbworker

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_LAST_AND_NAME.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "Отличное имя, запомню! Теперь укажи, пожалуйста, свой возраст.")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_AGE.value)

bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет! Как я могу к тебе обращаться?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_LAST_AND_NAME.value)
# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Что ж, начнём по-новой. Как тебя зовут?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_LAST_AND_NAME.value)

bot.infinity_polling()