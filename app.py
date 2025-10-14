import os
from flask import Flask, request
from clouddroid.bot import StreamBot  # your Pyrogram client

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json(force=True)
    StreamBot.process_updates([update])
    return "OK", 200

if __name__ == "__main__":
    # Run Flask on the PORT provided by Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
