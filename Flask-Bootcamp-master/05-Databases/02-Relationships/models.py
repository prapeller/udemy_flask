import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This grabs our directory
basedir = os.path.dirname(__file__)

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')  # 1-M
    owner = db.relationship('Owner', backref='puppy', uselist=False)  # 1-1

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"\tname: {self.name}\towner: {self.owner.name}\n"
        else:
            return f"\tname: {self.name}\towner: no owner\n"

    def report_toys(self):
        print(f"toys of {self.name}: {[toy.item_name for toy in self.toys]}")


class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))  # puppies.id because __tablename__='puppies

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))  # puppies.id because __tablename__='puppies

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
