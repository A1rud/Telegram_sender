import eel
import telebot

TOKEN = "you token"

bot = telebot.TeleBot(TOKEN)


@eel.expose
def send_message(chat_id, message):
    bot.send_message(chat_id, message)
    return "повідомлення відправлено"


eel.init("web")
eel.start("main.html", size=(400, 600))
