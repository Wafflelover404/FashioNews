import telebot

bot = telebot.TeleBot(token='')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("Get News !")



@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello, let's get right into fashion world !", reply_markup=keyboard)

bot.polling()