from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('puppy name: ')
    submit = SubmitField('add')


class DelForm(FlaskForm):
    id = IntegerField('puppy id: ')
    submit = SubmitField('delete')
