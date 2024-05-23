import telebot
import os
import re


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

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello, let's get right into fashion world !", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Get News !")
def bot_get_news(message):
    print("pressed !")
    os.system("python3 parser.py")
    bot.send_message(message.chat.id, "Here are some fresh news: ", reply_markup=keyboard)

    try:
        articles = read_and_split_articles("articles.txt")
        for i, article in enumerate(articles):
            print(f"Article {i + 1}:\n{article}\n")

    except FileNotFoundError:
        bot.send_message(message.chat.id, "Sorry, no news available right now.")

bot.polling()
