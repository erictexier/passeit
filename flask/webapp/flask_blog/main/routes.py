from flask import Blueprint
from flask import render_template, request
from flask_blog.models import Post

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5)
    return render_template("posts/home.html", title = 'Posts', posts = posts)

@main.route("/about")
def about():
    return render_template("main/about.html", title = 'About')