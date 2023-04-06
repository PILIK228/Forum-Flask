from flask import Blueprint
from flask import render_template

from models import Post
#конструктор класса блюпринт
posts = Blueprint('posts',__name__, template_folder='templates')


@posts.route('/')
def index():
    # получаем списоk постов
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)
