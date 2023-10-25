
from flask import render_template, request, Blueprint
from twitter.models import Post
# from PIL import Image 



main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    # posts = Post.query.all() #grab all obj from db
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page = page )
    return render_template('home.html', posts = posts)


@main.route("/about")
def about():
      posts = Post.query.all() #grab all obj from db
      return render_template('about.html', posts = posts, title='about')

