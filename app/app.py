# описание приложения
from flask import Flask
from config import Configuration

from posts.blueprint import posts #импортируем экземпрляр класса блюпринт

app = Flask(__name__)
app.config.from_object(Configuration) # передача в словарь конфиг настройки приложения через метод from_object (передаем класс Configuration)

app.register_blueprint(posts, url_prefix='/blog')