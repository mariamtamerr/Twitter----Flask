from datetime import datetime
from twitter import db, login_manager ##### 
# from flask_login import UserMixin
# db = SQLAlchemy()

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
    

    @classmethod
    def create_user(cls, request_form):
        user = cls(**request_form)
        db.session.add(user)
        db.session.commit()
        return user 

    # @classmethod
    # def create_user(cls, **kwargs):
    #     try:
    #         user = cls(**kwargs)
    #         print("User object before adding to the database:", user)
    #         db.session.add(user)
    #         db.session.commit()
    #         print("User object after adding to the database:", user)
    #         return user
    #     except Exception as e:
    #         db.session.rollback()
    #         print(f"Error creating user: {e}")
    #         return None



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Post( '{self.title}' ,'{self.date_posted}' )"



    @classmethod
    def create_post(cls, request_form):
        post = cls(**request_form)
        db.session.add(post)
        db.session.commit()
        return post 

    # @classmethod
    # def create_post(cls, request_form, user_id):
    #     post = cls(**request_form, user_id=user_id)
    #     db.session.add(post)
    #     db.session.commit()
    #     return post
