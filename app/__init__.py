from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql://action@localhost/project1_2
db = SQLAlchemy(app)

from app import views, models
