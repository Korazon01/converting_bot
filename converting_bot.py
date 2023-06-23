import requests
from bs4 import BeautifulSoup
import telebot

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
hi, I am a telegram bot that converts dollars into rubles and shows for how many rubles you can buy dollars at a given time.\
""")
    bot.reply_to(message,"please write the number")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    e = message.text

    a = 'https://quote.rbc.ru/ticker/59111/'
    b = requests.get(a).text
    soup = BeautifulSoup(b, 'lxml')
    block = soup.find(class_='chart__info__sum').text
    block = block.replace('₽', '')
    block = block.replace(',', '.')
    block = float(block)

    try:
        bot.reply_to(message,f'for that amount of dollars- {int(e)} , you can get - {block * int(e)} rubles')
        bot.reply_to(message, 'Also you can change in - https://www.bestchange.ru/')
    except:
        bot.reply_to(message, 'excuse me but you  did not write a number')



bot.infinity_polling()
