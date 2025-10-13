from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'clouddroid'

if __name__ == "__main__":
    # Get port from environment (Render sets this automatically)
    port = int(os.environ.get("PORT", 8080))
    # Bind to 0.0.0.0 so Render can detect it
    app.run(host="0.0.0.0", port=port)
