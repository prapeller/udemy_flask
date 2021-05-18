import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'adopt_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from source.owners.views import owners_blueprint
from source.puppies.views import puppies_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')