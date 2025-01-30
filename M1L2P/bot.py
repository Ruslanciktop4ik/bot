from config import TOKEN
import telebot
from random import choice
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
Команды:
                 /start - старт
                 /help - помощь
                 /info - информация
                 P.S тут так мало команд так как это тест бот\
""")


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    bot.reply_to(message, "о прикольная фоточка")


@bot.message_handler(commands=['fact'])
def fact_handler(message):
    fact = choice(["Древние римляне чистили зубы высушенными и измельченными мозгами мышей вместо зубной пасты.", "Интересные факты о нашем теле. Человеческий мозг не обрабатывает даже 10% поступающей в него информации.", "Когда эскимосские дети болеют простудой, их матери высасывают сопли губами прямо из их носа.", "50% бутилированной воды в мире на самом деле обычная вода из под крана, подвергнутая фильтрации."])
    bot.reply_to(message, fact)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()