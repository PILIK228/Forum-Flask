# app description
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate



app = Flask(__name__)
# передача в словарь конфиг настройки приложения через метод from_object (передаем класс Configuration)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db)
