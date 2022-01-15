from flask import render_template
from app import app 
from app.models import UserModel, TweetModel, CommentModel

@app.route('/',methods = ["GET"])
def home():
    tweet_model = TweetModel()
    return tweet_model.get_tweets()

@app.route('/',methods = ["POST"])
def post_tweet():
    tweet_model = TweetModel()
    return tweet_model.get_tweets()

@app.route('/{id}',methods = ["POST"])
def post_comment():
    tweet_model = TweetModel()
    return tweet_model.get_tweets()

@app.route('/{id}',methods = ["GET"])
def get_comment():
    tweet_model = TweetModel()
    return tweet_model.get_tweets()