"""
The end point of the platform that run the app, and
it register other blueprints(components), i.e: user component.
"""

from flask import Flask
from user import user_blueprint
app = Flask(__name__)
app.register_blueprint(user_blueprint)


