from flask import Flask, request
from bot import bot
from config import BOT_API

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
    bot.polling()
    app.run(host='0.0.0.0', port=8080)