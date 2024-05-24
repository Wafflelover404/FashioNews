import telebot
import os
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def read_and_split_articles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    articles = re.findall(r'\{(.*?)\}', content, re.DOTALL)
    articles = [article.strip() for article in articles]
    return articles

# Replace with your actual token
bot_token = ''
bot = telebot.TeleBot(token=bot_token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("Get News !")

articles = read_and_split_articles("articles.txt")

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello, let's get right into the fashion world!", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Get News !")
def bot_get_news(message):
    os.system("python3 parser.py")
    if articles:
        send_article(message.chat.id, 0)
    else:
        bot.send_message(message.chat.id, "Sorry, no news available right now.")

def send_article(chat_id, index):
    if 0 <= index < len(articles):
        markup = InlineKeyboardMarkup()
        markup.row(
            InlineKeyboardButton("« 1", callback_data="goto_0") if index > 0 else InlineKeyboardButton("· 1 ·", callback_data="stay"),
            InlineKeyboardButton(f"‹ {index}", callback_data=f"goto_{max(index-1, 0)}") if index > 0 else InlineKeyboardButton("· · ·", callback_data="stay"),
            InlineKeyboardButton(f"· {index+1} ·", callback_data="stay"),
            InlineKeyboardButton(f"{index+2} ›", callback_data=f"goto_{min(index+1, len(articles)-1)}") if index < len(articles) - 1 else InlineKeyboardButton("· · ·", callback_data="stay"),
            InlineKeyboardButton(f"{len(articles)} »", callback_data=f"goto_{len(articles)-1}") if index < len(articles) - 1 else InlineKeyboardButton(f"· {len(articles)} ·", callback_data="stay")
        )

        bot.send_message(chat_id, articles[index], reply_markup=markup)
    else:
        bot.send_message(chat_id, "Sorry, no more articles available.")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("goto_"):
        index = int(call.data.split('_')[1])
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_article(call.message.chat.id, index)
    elif call.data == "update":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot_get_news(call.message)
    elif call.data == "current":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_article(call.message.chat.id, int(call.message.text.split(':')[0].split()[-1])-1)

bot.polling()
