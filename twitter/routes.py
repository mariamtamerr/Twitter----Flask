



from flask import render_template, url_for, redirect, flash, session, abort, request
from twitter import app, db , bcrypt  
from twitter.forms import RegistrationForm, LoginForm, PostForm
from twitter.models import User, Post
# from PIL import Image 
# from flask_login import login_user, current_user, logout_user
from flask_login import current_user, login_required, login_user




# posts = [
#     {
#         'author' : 'Mariam Tamer',
#         'title': 'Blog Post 1',
#         'content': 'First Post ',
#         'created_at': '21 Oct, 2023'
#     } , 

#      {
#         'author' : 'Menna Tamer',
#         'title': 'Blog Post 2',
#         'content': 'Second Post ',
#         'created_at': 'August 21, 2018'
#     } , 

#      {
#         'author' : 'Nesma Moahmed',
#         'title': 'Blog Post 3',
#         'content': 'Third Post ',
#         'created_at': '5 April, 2015'
#     } , 
# ]



@app.route("/")
@app.route("/home")
def home():
    # posts = Post.query.all() #grab all obj from db
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page = page )
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
      posts = Post.query.all() #grab all obj from db
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
            login_user(user)
            flash("You've been logged in successfully!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Incorrect username or password", 'danger')
    return render_template('login.html',title='login', form=form) #pass the form as an arguments


# @app.route("/logout")
# def logout():
#     return redirect(url_for('home'))



@app.route("/account")
@login_required
def account():
    image = url_for('static', filename='images/'+ current_user.image )
    return render_template('account.html',title='Account', image=image)


@app.route("/post/new", methods=['GET', 'POST']) #accepting a POST request to redirect you to different route aka home page 
@login_required
def new_post():
    form = PostForm() #make an instance of the form
    if form.validate_on_submit():
        # if current_user.is_authenticated:
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('You tweet has been sent', 'primary')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


# a route that takes us a specific page of a specific tweet
@app.route('/post/<int:post_id>', methods=['GET','POST'])
def post(post_id):
    # post = Post.query.get(post_id)  yalla nst3ml wahda gdeda
    post = Post.query.get_or_404(post_id) #either get it or get error 404 and if it's there then render the following template
    return render_template('post.html', title=post.title, post=post)





@app.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm() #make an instance of the form
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        # post = Post(title=form.title.data, content=form.content.data, author=current_user)
        # db.session.add(post) we don't need it bc they're already in the db 
        db.session.commit() #we just wanna update / commit them
        flash('Your Tweet Has Been Updated', 'success')
        # return redirect(url_for('home'))
        form.title.data = post.title # so when i open the update page , i can find the current title and content
        form.content.data = post.content #############
        return redirect(url_for('post', post_id=post.id)) #return for that specific id post
    elif request.method=='GET':
        form.title.data = post.title # so when i finish updating, i can see my changes aka current new title and content
        form.content.data = post.content #############
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST']) # POST request only received from the modal
@login_required 
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Tweet Has Been Deleted', 'success')
    return redirect(url_for('home'))
  
    


@app.route("/users/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404() #next in posts you must specify that author=user so you et total posts of a specific user not all posts of all users cmobined 
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc()).paginate(per_page=5, page = page )
    return render_template('user_posts.html', posts = posts, user=user)
