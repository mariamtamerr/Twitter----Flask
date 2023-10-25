

from flask import render_template, url_for, redirect, flash, session, abort, request, Blueprint
from twitter import app, db , bcrypt  
from twitter.posts.forms import RegistrationForm, LoginForm, PostForm
from twitter.models import User, Post
# from PIL import Image 
from flask_login import current_user, login_required, login_user


posts = Blueprint('posts')




@posts.route("/post/new", methods=['GET', 'POST']) #accepting a POST request to redirect you to different route aka home page 
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
@posts.route('/post/<int:post_id>', methods=['GET','POST'])
def post(post_id):
    # post = Post.query.get(post_id)  yalla nst3ml wahda gdeda
    post = Post.query.get_or_404(post_id) #either get it or get error 404 and if it's there then render the following template
    return render_template('post.html', title=post.title, post=post)





@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
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


@posts.route('/post/<int:post_id>/delete', methods=['POST']) # POST request only received from the modal
@login_required 
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Tweet Has Been Deleted', 'success')
    return redirect(url_for('home'))
  
   