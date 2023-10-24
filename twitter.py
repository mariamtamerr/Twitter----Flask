from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash, session 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
# import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECRET_KEY'] = '13992d730c4efd613a11ed4b6a65e51c'   #python --> import secrets --> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # 3 slashes for the relative path

db = SQLAlchemy(app) # an instance of your db

from forms import PostForm


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"Post( '{self.username}', '{self.email}' , '{self.image}' )"




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.Text(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post( '{self.title}' ,'{self.date_posted}' )"









posts = [
    {
        'author' : 'Mariam Tamer',
        'title': 'Blog Post 1',
        'content': 'First Post ',
        'created_at': '21 Oct, 2023'
    } , 

     {
        'author' : 'Menna Tamer',
        'title': 'Blog Post 2',
        'content': 'Second Post ',
        'created_at': 'August 21, 2018'
    } , 

     {
        'author' : 'Nesma Moahmed',
        'title': 'Blog Post 3',
        'content': 'Third Post ',
        'created_at': '5 April, 2015'
    } , 
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', posts = posts, title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm() #create an instance of your form that we're going to send to your application
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register', form=form) #pass the form as an arguments



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #create an instance of your form that we're going to send to your application
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '1234':
            flash("You've been logged in successfully!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Incorrect username or password", 'danger')
    return render_template('login.html',title='login', form=form) #pass the form as an arguments




@app.route("/create", methods=['GET', 'POST']) #accepting a POST request to redirect you to different route aka home page 
def new_post():
    form = PostForm() #make an instance of the form
    if form.validate_on_submit():
        flash('You tweet has been sent')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form)



if __name__ == "__main__":
    app.run(debug=True)