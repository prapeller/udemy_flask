import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'topsecret'


# db setup:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

# login configs:
logman = LoginManager()
logman.init_app(app)
logman.login_view = 'users.login'


# blueprints setup:
from source.core.views import core_blueprint
from source.users.views import users_blueprint
from source.error_pages.handlers import err_blueprint
from source.blogposts.views import blog_posts_blueprint

app.register_blueprint(core_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(err_blueprint)
app.register_blueprint(blog_posts_blueprint)
