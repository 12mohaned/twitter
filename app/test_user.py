"""
File than consists of unit tests for the below functions
API = '/home'(GET)
API = '/home/<tweet_id>'(GET)
API = '/home/<tweet_id>/<comment_id>'(GET)
"""
import pytest 
from flask.testing import FlaskClient 
from wsgi import app

def client():
    app.testing = True
    client=app.test_client()
    return client

def get_tweets():
    Client = client()
    response = Client.get('/home')
    return response.status_code

def get_tweet_comments(tweet_id):
    Client = client()
    response = Client.get('/home/'+str(tweet_id))
    return response.status_code

def get_tweet_subcomments(comment_id):
    Client = client()
    response = Client.get('/home/1'+str(comment_id))
    return response.status_code

def test_answer():
    #Test case with valid tweet id
    assert get_tweet_comments(1) == 200
    #Test case with in-valid tweet id
    assert get_tweet_comments(2) == 400
    #Test case with in-valid comment id
    assert get_tweet_subcomments(2) == 400
    #Test case with valid comment id
    assert get_tweet_subcomments("") == 200