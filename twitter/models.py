from datetime import datetime
from twitter import db, login_manager ##### 
# from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"Post( '{self.username}', '{self.email}' , '{self.image}' )"


    def get_id(self):
        return str(self.id)


    def is_active(self):
        return True  # You can implement logic to determine whether the user is active or not

    def is_authenticated(self):
        return True  # Return 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.Text(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post( '{self.title}' ,'{self.date_posted}' )"


