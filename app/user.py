from flask import render_template, Blueprint,jsonify, request
from models import UserModel, TweetModel, CommentModel
from controllers import UserController, TweetController, CommentController
import datetime

tweet_model = TweetModel()
tweet_controller = TweetController()
comment_model = CommentModel()
comment_controller = CommentController()
user_blueprint = Blueprint('user_blueprint', __name__)

#below variable act as Session object
Session = {'user_name' : 'user'}
username = Session['user_name']

@user_blueprint.route('/home',methods = ["GET"])
def home():
    tweets = tweet_model.get_tweets()
    return jsonify(tweets)

@user_blueprint.route('/home/<tweet_id>',methods = ["GET"])
def get_tweet_comments(tweet_id):  
    """
    This API returns the main comments on tweet.
    """
    response = comment_model.get_tweet_comments(tweet_id)
    return jsonify(response)

@user_blueprint.route('/home/<tweet_id>/<comment_id>',methods = ["GET"])
def get_sub_comments(tweet_id, comment_id):  
    """
    This API returns the sub comments on a comment.
    """
    response = ""
    if not(tweet_model.is_exists_tweet(tweet_id) is None):
        response = comment_model.get_sub_comments(comment_id)
    return jsonify(response)

@user_blueprint.route('/home',methods = ["POST"])
def post_tweet():
    content = request.form.get("content")
    if(tweet_controller.is_tweet_valid(content)):
        tweet_model.add_tweet(username, content,datetime.datetime.now)


@user_blueprint.route('/home/<tweet_id>',methods = ["POST"])
def post_comment(tweet_id):
    content = request.form.get("content")
    if not comment_controller.is_comment_empty(content):
        comment_model.add_comment(tweet_id, content, None)

@user_blueprint.route('/home/<tweet_id>/<parent_comment_id>',methods = ["POST"])
def post_sub_comment(tweet_id,parent_comment_id):
    content = request.form.get("content")
    if not comment_controller.is_comment_empty(content):
        comment_model.add_comment(tweet_id,content,parent_comment_id)
