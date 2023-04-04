# описание приложения
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Configuration) # передача в словарь конфиг настройки приложения через метод from_object (передаем класс Configuration)


db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')