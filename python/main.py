import telebot
print("dd")

token = "6956999719:AAE8NEB6-CZm3gmlpYEnbJarVBrgCZGpSFE"

bot = telebot.TeleBot(token)


@bot.message_handler({"start"})
def start(message):
    bot.reply_to(message,"welcomr")

bot.polling()
