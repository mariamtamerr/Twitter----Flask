
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
# from flask_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)  ######## NEW 

# app = Flask(__name__, static_url_path='/static')

# import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SECRET_KEY'] = '13992d730c4efd613a11ed4b6a65e51c'   #python --> import secrets --> secrets.token_hex(16)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # 3 slashes for the relative path

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ###### for the ap.context

db = SQLAlchemy(app) # an instance of your db
bcrypt = Bcrypt(app) # an instance of the Bcrypt class

# app.config['IPYTHON_CONFIG'] = {
#     'InteractiveShell': {
#         'colors': 'Linux',
#         'confirm_exit': False,
#     },
# }


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login' #blueprint users before it too

# app.app_context().push() ####### for the ap.context


# out it after app initializtaion 

# from twitter import app 
# from twitter import routes, app

from twitter.users.routes import users  #import from blueprint
from twitter.posts.routes import posts  #import from blueprint
from twitter.main.routes import main    #import from blueprint

app.register_blueprint(users)   #then register the blueprint
app.register_blueprint(posts)
app.register_blueprint(main)


app.app_context().push() ####### for the ap.context
