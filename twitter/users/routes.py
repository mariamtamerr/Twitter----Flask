
import secrets
from flask import render_template, url_for, redirect, flash, session, abort, request, Blueprint
from werkzeug.utils import secure_filename
import os
from twitter import app, db , bcrypt  
from twitter.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from twitter.models import User, Post
# from PIL import Image 
from flask_login import current_user, login_required, login_user, logout_user

users = Blueprint('users', __name__)




@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm() #create an instance of your form that we're going to send to your userslication
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in','success')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='register', form=form) #pass the form as an arguments



@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #create an instance of your form that we're going to send to your application
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() #filter by username to check if this username exists
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if it does exist and the bcrypt pass is checked then import the user login function
            login_user(user)
            flash("You've been logged in successfully!", 'success')
            return redirect(url_for('main.home'))
        else:
            flash("Incorrect username or password", 'danger')
    return render_template('login.html',title='login', form=form) #pass the form as an arguments





@users.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('main.home'))





# def save_picture(form_picture):
#      random_hex = secrets.token_hex(8)
#      f_name, f_ext = os.path.split(form_picture.filename)
#      picture_fn = random_hex + f_ext
#      picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
#      form_picture.save(picture_path)
#      return picture_fn


# @users.route("/account", methods=["GET", "POST"])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             profile_file = save_picture(form.image.data)
#             current_user.image = profile_file 
#         current_user.username = form.username.data 
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('Successfully Updated Account', 'info')
#         return redirect(url_for('users.account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image = url_for('static', filename='images/'+ current_user.image )
#     return render_template('account.html',title='Account', image=image, form=form)




@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.image.data:
            original_filename = form.image.data.filename
            filename =  secure_filename(original_filename)
            picture_path = os.path.join(app.root_path, 'static/images', filename)
            form.image.data.save(picture_path)
            current_user.image = original_filename
        current_user.username = form.username.data 
        current_user.email = form.email.data
        db.session.commit()
        flash('Successfully Updated Account', 'info')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='images/'+ current_user.image )
    return render_template('account.html',title='Account', image=image, form=form)





@users.route("/users/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404() #next in posts you must specify that author=user so you et total posts of a specific user not all posts of all users cmobined 
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc()).paginate(per_page=5, page = page )
    return render_template('user_posts.html', posts = posts, user=user)

