# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:34:26 2026

@author: Bo'ltakov Diyor
Kiril-Lotin, Lotin-Kiril  Telegram bot
"""

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = 'TOKEN_NI_BU_YERGA_YOZING'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()