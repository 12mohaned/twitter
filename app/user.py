import datetime
from flask import render_template, Blueprint, jsonify, request, abort
from models import UserModel, TweetModel, CommentModel
from controllers import UserController, TweetController, CommentController
import json

tweet_model = TweetModel()
tweet_controller = TweetController()
comment_model = CommentModel()
comment_controller = CommentController()
user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/home', methods=["GET"])
def home():
    tweets = tweet_model.get_tweets()
    return render_template("home.html", tweets = tweets)

@user_blueprint.route('/home/<tweet_id>', methods=["GET"])
def get_tweet_comments(tweet_id):
    """
    This API returns the main comments on tweet.
    """
    comments = comment_model.get_tweet_comments(tweet_id)
    if not tweet_model.is_exists_tweet(tweet_id) :
        abort(400, "Tweet is not found")
    return jsonify({'comments':comments})

@user_blueprint.route('/home/<tweet_id>/<comment_id>', methods=["GET"])
def get_sub_comments(tweet_id, comment_id):
    """
    This API returns the sub comments on a comment.
    """
    comments = ""
    if tweet_model.is_exists_tweet(tweet_id) is None:
        abort(400, "Tweet is not found")

    if len(comment_model.get_sub_comments(comment_id)) == 0:
        abort(400, "Comment is not found")

    comments = comment_model.get_sub_comments(comment_id)
    return jsonify({'comments':comments})

@user_blueprint.route('/home', methods=["POST"])
def post_tweet():
    #Content is fetched from tweet form(UI)
    content = request.form.get('tweet')
    if(tweet_controller.is_tweet_valid(content)):
        tweet_model.add_tweet("mohaned",content,datetime.datetime.now())
    else:
        abort(400, "Please make sure, tweet format is followed")
    return render_template("home.html")


@user_blueprint.route('/home/<tweet_id>', methods=["POST"])
def post_comment(tweet_id):
    #Content is fetched from comment form(UI)
    content = request.form.get("comment")
    if comment_controller.is_comment_empty(content):
        abort(400, "Comment can not be empty")
    comment_model.add_comment(tweet_id, content, None,"mohaned")   
    return abort(200, "Comment is posted")

@user_blueprint.route('/home/<tweet_id>/<parent_comment_id>', methods=["POST"])
def post_sub_comment(tweet_id, parent_comment_id):
    #Content is fetched from comment form(UI)
    content = request.form.get("comment")
    if comment_controller.is_comment_empty(content):
        abort(400, "Comment can not be empty")
    comment_model.add_comment(tweet_id, content, parent_comment_id, "mohaned")
    return abort(200, "Comment is posted")
