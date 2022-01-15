from flask import render_template, Blueprint,jsonify, request
from models import UserModel, TweetModel, CommentModel
from controllers import UserController, TweetController, CommentController
import datetime

tweet_model = TweetModel()
tweet_controller = TweetController()
comment_model = CommentModel()
comment_controller = CommentController()
user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/',methods = ["GET"])
def home():
    tweets = tweet_model.get_tweets()
    return jsonify(tweets)

