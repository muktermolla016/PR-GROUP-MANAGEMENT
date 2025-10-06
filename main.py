from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
from handlers import register_all_handlers
from db import db
import threading
import os
from flask import Flask

logging.basicConfig(level=logging.INFO)

app = Client(
    "group_manger_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_all_handlers(app)

print("Bot is starting...")

# --- Flask Web Server for Render ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Pr Group Manager Bot is running successfully!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

# Run both bot and web server together
threading.Thread(target=lambda: app.run()).start()
threading.Thread(target=run_web).start()
