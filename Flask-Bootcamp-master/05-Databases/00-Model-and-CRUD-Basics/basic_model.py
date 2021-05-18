import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(__file__)

app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# We inherit from db.Model class
class Puppy(db.Model):
    # If you don't provide this, the default table name will be the class name
    __tablename__ = 'puppies'

    # Now create the columns, Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # This sets what an instance in this table will have, note the id will be auto-created for us later, so we don't add it here!
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # string representation of a puppy in the model
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
