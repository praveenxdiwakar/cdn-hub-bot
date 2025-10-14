# app.py
import threading
import asyncio
from flask import Flask, send_file, abort, request
from clouddroid.bot import StreamBot
from clouddroid.server.stream_routes import get_file_path  # Make sure this exists

app = Flask(__name__)

# ------------------------------
# Flask Routes
# ------------------------------

@app.route('/')
def home():
    return "✅ CloudDroid is Live — Pyrogram + Flask working!"

@app.route('/stream/<file_id>')
def stream_file(file_id):
    """Stream file by file_id."""
    try:
        file_path = get_file_path(file_id)  # Your function should return absolute path
        if file_path:
            return send_file(file_path, as_attachment=False)
        else:
            return abort(404, description="File not found")
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

@app.route('/file/<path:file_path>')
def download_file(file_path):
    """Direct download link."""
    try:
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return abort(404, description="File not found")
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

# ------------------------------
# Pyrogram Bot Thread
# ------------------------------

def run_pyrogram():
    print("🚀 Starting Pyrogram Bot...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    StreamBot.run()

# ------------------------------
# Main
# ------------------------------

if __name__ == "__main__":
    # Start Pyrogram in a separate thread
    bot_thread = threading.Thread(target=run_pyrogram)
    bot_thread.start()

    # Start Flask server
    print("🌐 Starting Flask server...")
    app.run(host="0.0.0.0", port=10000)
