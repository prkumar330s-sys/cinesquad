# CinemaSquad Full Website
# Run with: python app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CinemaSquad App Running!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)

