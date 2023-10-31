
from flask import render_template, request, Blueprint
# from twitter.models import Post
# from PIL import Image 
from twitter.models import Post, User
import random
from sqlalchemy import func  


main = Blueprint('main', __name__)



# @main.route("/")
# @main.route("/home")
# def home():
#     # posts = Post.query.all() #grab all obj from db
#     page = request.args.get('page', 1, type=int)
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page = page )
#     return render_template('home.html', posts = posts)


@main.route("/")
@main.route("/home")
def home():
    # 3 random usernames for the people you may know sidebar
    random_users = User.query.order_by(func.random()).limit(3).all()
    # posts pagination in home page .. 5 posts per page
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    
    return render_template('home.html', posts=posts, random_users=random_users)




@main.route("/about")
def about():
      posts = Post.query.all() #grab all obj from db
      return render_template('about.html', posts = posts, title='about')

