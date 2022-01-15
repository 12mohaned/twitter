from app import app
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    tweet_model = TweetModel()
    return tweet_model.get_tweets()


