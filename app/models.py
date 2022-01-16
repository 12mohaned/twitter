from config import connect
import datetime
connection = connect()
cursor = connection.cursor()

"""
Class responsible for handling crud operations of database tables.
"""

class UserModel:
    """
    Module responsible for crud operations of table "account".
    """
    def add_user(self, username, name, email):
        cursor.execute("INSERT INTO account (username, name, email) VALUES (%s, %s, %s)", (username, name, email))
        connection.commit()
        return cursor.statusmessage
    def is_user_exists(self, username):
        cursor.execute("select * from account where username = %s",(username,))
        return cursor.fetchone()


class TweetModel:
    """
    Model responsible for crud operations of table "tweet".
    """
    def add_tweet(self, username, content, time_posted):
        cursor.execute("INSERT INTO tweet (username, description, time_posted) VALUES (%s, %s, %s)",
                       (username, content, time_posted))
        connection.commit()
        return cursor.statusmessage
    def get_tweets(self):
        cursor.execute('Select * from tweet ORDER by time_posted DESC')
        return cursor.fetchall()
    def get_tweet_comments(self, tweet_id):
        comment_model = CommentModel()
        return comment_model.get_tweet_comments(tweet_id)
    def is_exists_tweet(self, tweet_id):
        cursor.execute("Select id from tweet where id = %s", (tweet_id))
        return cursor.fetchone()

class CommentModel:
    """
    Model responsible for crud operations of table "comment".
    """
    def add_comment(self, tweet_id, content, parent_commend_id):
        cursor.execute("INSERT INTO comment (tweet_id, content, parent_commend_id) VALUES (%s, %s, %s)"
                       ,(tweet_id, content, parent_commend_id))
        connection.commit()
        return cursor.statusmessage
    def get_tweet_comments(self, tweet_id):
        cursor.execute('Select * from comment where tweet_id = %s',[tweet_id])
        return cursor.fetchall() 
    def get_sub_comments(self, parent_id):
        cursor.execute('Select * from comment where parent_commend_id = %s',[parent_id])
        return cursor.fetchall() 

    