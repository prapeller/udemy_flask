from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from source.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('cnfrm_password', 'pass should match')])
    cnfrm_password = PasswordField('Cnfrm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    @staticmethod
    def check_email(email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('This email has been registered already!')

    @staticmethod
    def check_username(username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('This username has been registered already!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    @staticmethod
    def check_email(email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('This email has been registered already!')

    @staticmethod
    def check_username(username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('This username has been registered already!')

