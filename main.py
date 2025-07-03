from simpleeval import simple_eval
import os
from dotenv import load_dotenv
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет,Я ваш калькулятор-помощник!')

@bot.message_handler(func=lambda message: True)
def calculator(message):
    try:
        expression = message.text
        result = simple_eval(expression)
        bot.send_message(message.chat.id,f"Ваш результат: {result}")
    except Exception as e:
        bot.reply_to(message, 'Ошибка,вы ввели несуществующее выражение!')


bot.polling(none_stop=True)


