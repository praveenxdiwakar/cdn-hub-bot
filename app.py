# app.py
import threading
import asyncio
from flask import Flask
from clouddroid.bot import StreamBot

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CloudDroid is Live — Pyrogram + Flask working!"

def run_pyrogram():
    print("🚀 Starting Pyrogram Bot...")
    # Create a new event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    StreamBot.run()

if __name__ == "__main__":
    # Run the Pyrogram bot in a background thread
    bot_thread = threading.Thread(target=run_pyrogram)
    bot_thread.start()

    # Run Flask server
    print("🌐 Starting Flask server...")
    app.run(host="0.0.0.0", port=10000)
