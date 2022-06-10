import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#app = Flask(__name__, static_url_path='', static_folder='static')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images'

#print("**", app.config)
db = SQLAlchemy(app)
