API = '7477387899:AAHltCgLvQa7wZAt8zocfGJGp7QtvUSpv3A'
ADMIN = 1210146115
bot = ''
# -----------------------------------------------------------
import telebot
import subprocess
import os
import sys
import time

bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message): # команда /start
    if message.from_user.id == ADMIN:
        bot.send_message(message.chat.id, "Привет!")
    else:
        bot.send_message(message.chat.id, "У вас нет прав для использования этого бота.")

@bot.message_handler(commands=['shutdown'])
def shutdown_bot(message):
    if message.from_user.id == ADMIN:
        bot.send_message(message.chat.id, "Выключение...")
        os.system("shutdown /s /t 1")  # Команда для выключения Windows
    else:
        bot.send_message(message.chat.id, "У вас нет прав для использования этого бота.")

print("Бот запущен...")
bot.send_message(ADMIN, "Управление доступно...")
bot.polling()