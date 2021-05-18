from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from source.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Passowrds must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        # (if User.query.filter_by(email=field.data).first is not None, alredy exists user with such email
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Your email already registered!')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Your username already registered')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login!')
