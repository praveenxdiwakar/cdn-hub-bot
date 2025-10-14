# app.py
import threading
from flask import Flask
from clouddroid.bot import StreamBot

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CloudDroid Bot is running!"

# --- Run Pyrogram Bot in a Background Thread ---
def run_pyrogram():
    print("🚀 Starting Pyrogram Bot...")
    StreamBot.run()

if __name__ == "__main__":
    # Start Pyrogram bot on another thread
    bot_thread = threading.Thread(target=run_pyrogram)
    bot_thread.start()

    # Start Flask for web streaming
    print("🌐 Starting Flask server...")
    app.run(host="0.0.0.0", port=10000)
