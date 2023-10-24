



from flask import render_template, url_for, redirect, flash, session 
from twitter import app, db , bcrypt  
from twitter.forms import RegistrationForm, LoginForm, PostForm
from twitter.models import User, Post
# from flask_login import login_user





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
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='register', form=form) #pass the form as an arguments



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #create an instance of your form that we're going to send to your application
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() #filter by username to check if this username exists
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if it does exist and the bcrypt pass is checked then import the user login function
            # login_user(user, remember=form.remember.data)
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
