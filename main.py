from flask import Flask, request
import os
from dotenv import load_dotenv
from bot import bot

load_dotenv()

BOT_API = os.getenv("BOT_API")

app = Flask(__name__)

@app.route('/' + BOT_API, methods=['POST'])
def handle_webhook():
    update = request.get_json()
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "!", 200

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    bot.remove_webhook()
    # bot.polling()
    app.run(host='0.0.0.0', port=5000)