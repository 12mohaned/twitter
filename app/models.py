"""
File that contain classes responsible for crud operations of database tables.
"""

from config import connect
connection = connect()
cursor = connection.cursor()

class UserModel:
    """
    Module responsible for crud operations of table "account".
    """

    def add_user(self, username, name, email):
        """
        param data: username
        type  data: string
        param data: name
        type  data: string
        param data: email
        type  data: string
        """
        query = "INSERT INTO account (username, name, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, name, email))
        connection.commit()
        return cursor.statusmessage

    def is_user_exists(self, username):
        """
        param data: username
        type  data: string
        """
        query = "select * from account where username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone()

class TweetModel:
    """
    Model responsible for crud operations of table "tweet".
    """

    def add_tweet(self, username, content, time_posted):
        """
        param data: username
        type  data: string
        param data: content
        type  data: string
        param data: time_posted
        type  data: datetime
        """
        query = "INSERT INTO tweet (username, description, time_posted) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, content, time_posted))
        connection.commit()
        return cursor.statusmessage

    def get_tweets(self):
        query = 'SELECT * from tweet ORDER by time_posted DESC'
        cursor.execute(query)
        return cursor.fetchall()

    def get_tweet_comments(self, tweet_id):
        """
        param data: tweet_id
        type  data: int
        """
        comment_model = CommentModel()
        return comment_model.get_tweet_comments(tweet_id)

    def is_exists_tweet(self, tweet_id):
        """
        param data: tweet_id
        type  data: int
        """
        query = "SELECT id from tweet where id = %s"
        cursor.execute(query, (tweet_id))
        return cursor.fetchone()

class CommentModel:
    """
    Model responsible for crud operations of table "comment".
    """

    def add_comment(self, tweet_id, content, parent_commend_id):
        """
        param data: tweet_id
        type  data: int
        param data: content
        type  data: string
        param data: parent_commend_id
        type  data: int
        """
        query = "INSERT INTO comment (tweet_id, content, parent_commend_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (tweet_id, content, parent_commend_id))
        connection.commit()
        return cursor.statusmessage

    def get_tweet_comments(self, tweet_id):
        """
        param data: tweet_id
        type  data: int
        """
        query = 'SELECT * from comment where tweet_id = %s'
        cursor.execute(query, [tweet_id])
        return cursor.fetchall()

    def get_sub_comments(self, parent_id):
        """
        Return sub-comment(s) of the parent comment
        param data: parent_id
        type  data: int
        return: sub comment(s) of the comment.
        """
        query = 'SELECT * from comment where parent_commend_id = %s'
        cursor.execute(query, [parent_id])
        return cursor.fetchall()
