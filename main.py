from flask import Flask, request
import os
from dotenv import load_dotenv
from bot import bot, BOT_API
import telebot

load_dotenv()

app = Flask(__name__)

@app.route('/' + BOT_API, methods=['POST'])
def handle_webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return "ok", 200

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook(url=f"https://telegram-bot4.onrender.com/{BOT_API}")
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
