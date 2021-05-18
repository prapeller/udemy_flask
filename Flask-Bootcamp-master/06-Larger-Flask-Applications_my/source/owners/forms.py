from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('owner name: ')
    puppy_id = IntegerField('puppy id: ')
    submit = SubmitField('add owner')