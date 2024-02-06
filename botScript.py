import os
import telebot
import json
from getStockPrice import get_stock_price

def botRunner():
    data = {}
    with open('credentials.json') as json_file:
        data['api_token'] = json.load(json_file)['telegram_api_token']

    BOT_TOKEN = data['api_token']
    bot = telebot.TeleBot(BOT_TOKEN)

    # A global variable to store the user input
    user_input = None

    # A message handler that responds to the /start command
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Hello, I can help you get the current price of the stock. Please enter the symbol of the stock")

    # A message handler that responds to any text message
    @bot.message_handler(func=lambda msg: True)
    def get_user_input(message):
        global user_input
        user_input = message.text
        print(f"get_user_input function called {user_input}")
        data = get_stock_price(user_input) 
        price = data["05. price"]
        bot.reply_to(message, f"Stock Symbol : {message.text} \nStock Price : {price}")

    # Start the bot
    bot.polling()

botRunner()