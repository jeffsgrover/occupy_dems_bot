from os import environ
from flask import Flask
import twitter_bot

app = Flask(__name__)

@app.route("/")
def home():
    twitter_bot.post_tweet()
    return "Posting a tweet..."

app.run(host='0.0.0.0', port=environ.get('PORT'))
