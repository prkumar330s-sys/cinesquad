# CinemaSquad Full Website
# Run with: python app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CinemaSquad App Running!"

if __name__ == '__main__':
    app.run(debug=True)
