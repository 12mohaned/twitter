from flask import Flask
from user_blueprint import user_blueprint 

app = Flask(__name__)
app.register_blueprint(user_blueprint)