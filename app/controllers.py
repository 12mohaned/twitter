from models import UserModel, CommentModel, TweetModel
import re

"""
Controller acts as middleware between views and model, to validate data to enusre
consistency and integrity.
"""

class UserController:
    """
    responsible for validation and execution of UserModel.
    """
    def is_username_valid(self, username):
        is_username_exists = UserModel.is_user_exists(username)
        return len(username)  <= 14 and  len(username) > 0 and (not is_username_exists)
    def is_name_valid(self, name):
        return len(name)  <= 15 and  len(name) > 0
    def is_email_valid(self, email):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(email_regex, email)

class TweetController:
    """
    Responsible for validation and execution of TweetModel.
    """
    def is_tweet_valid(self, content):
        return len(content)  <= 140 and  len(content) > 0

class CommentController:
    """
    Responsible for validation and execution of CommentModel.
    """
    def is_comment_empty(self, content):
        return len(content) == 0