import telebot
import subprocess

bot = telebot.TeleBot(token='')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("Get News !")



@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello, let's get right into fashion world !", reply_markup=keyboard)

@bot.message_handler(commands=['Get News !'])
def bot_start(message):
    bot.send_message(message.chat.id, "Here are some fresh news: ", reply_markup=keyboard)
    w = open('articles.txt', 'r')
    articles = w.readlines()
    bot.send_message(message.chat.id, articles)
bot.polling()