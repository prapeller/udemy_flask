from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddPupForm(FlaskForm):
    name = StringField('puppy name: ')
    submit = SubmitField('add')


class DelPupForm(FlaskForm):
    id = IntegerField('puppy id: ')
    submit = SubmitField('delete')


class AddOwnerForm(FlaskForm):
    name = StringField('owner name: ')
    pup_id = IntegerField('puppy id: ')
    submit = SubmitField('add')
