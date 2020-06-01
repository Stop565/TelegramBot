import telebot
from telebot import types

TOKEN = '1222056736:AAGbrbh7iM7l72KFj_4_NbqOrbY9ZFPr7fw' # bot token from @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)



bot.polling(none_stop=True)
