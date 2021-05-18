import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.dirname(__file__)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydata.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# set FLASK_APP=app_base.py
# flask db init
# flask db migrate -m "created puppy table"
# flask db upgrade


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    breed = db.Column(db.Text)
    # flask db migrate -m "added breed column"
    # flask db upgrade

    def __init__(self, id, name, age, breed):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f'\tid: {self.id}\tname: {self.name}\tage: {self.age}\tbreed: {self.breed}\n'

