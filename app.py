from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from flask import Flask, request
import requests
import os
from telegram import Bot, Update

from main import (
    start,
    photo,
    shop,
    get_cart,
    about,
    contact,
    phone_list,
    phone,
    add_cart,
    query
)

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/api', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'hi from Python-2022I'
    # get data from request
    else:
        data = request.get_json(force=True)

        # update
        dispatcher: Dispatcher = Dispatcher(bot, None, workers=0)
        update: Update = Update.de_json(data, bot)
        
        dispatcher.add_handler(CommandHandler('start', callback=start))
        dispatcher.add_handler(MessageHandler(Filters.photo,photo))
        dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'),shop))
        dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'),get_cart))
        dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
        dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
        dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
        dispatcher.add_handler(CallbackQueryHandler(phone_list,pattern='phone_list'))
        dispatcher.add_handler(CallbackQueryHandler(phone,pattern='phone'))
        dispatcher.add_handler(CallbackQueryHandler(add_cart,pattern='add_cart'))
        dispatcher.add_handler(CallbackQueryHandler(query))

        dispatcher.process_update(update)
        return 'ok'