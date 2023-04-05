from flask import Blueprint
from flask import render_template

#конструктор класса блюпринт
posts = Blueprint('posts',__name__, template_folder='templates')


@posts.route('/')
def index():
    # получаем списоr постов
    return render_template('posts/index.html')
