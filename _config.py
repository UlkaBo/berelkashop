from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'qweasdzxc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#print("**", app.config)
db = SQLAlchemy(app)
