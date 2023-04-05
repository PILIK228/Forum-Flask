from app import app
from flask import render_template

# декоратор, обращаемся к экземляру класса Фласк, методу роут - '/' - корень сайта, главная страница
@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)