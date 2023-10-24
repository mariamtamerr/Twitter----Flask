
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECRET_KEY'] = '13992d730c4efd613a11ed4b6a65e51c'   #python --> import secrets --> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # 3 slashes for the relative path

db = SQLAlchemy(app) # an instance of your db

# out it after app initializtaion 

from twitter import routes 


