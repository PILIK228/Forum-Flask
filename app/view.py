from app import app
from flask import render_template
@app.route('/') # декоратор, обращаемся к экземляру класса Фласк, методу роут - '/' - корень сайта, домен второго уровня
def index():
    return render_template('index.html')