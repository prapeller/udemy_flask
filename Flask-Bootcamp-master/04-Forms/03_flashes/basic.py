from flask import Flask, flash, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mykey'
app.secret_key = 'mykey'


class SimpleForm(FlaskForm):
    breed = StringField('enter your breed ', validators=[DataRequired()])
    button = SubmitField('Ok')


@app.route('/', methods=['GET', 'POST'])
def index():
    simple_form = SimpleForm()

    if simple_form.validate_on_submit():
        # session['breed'] = simple_form.breed.data
        # flash(f'the breed you entered: {session["breed"]}')
        flash(f'the breed you entered: {simple_form.breed.data}')

        return redirect(url_for('index'))

    return render_template('index.html', form=simple_form)


if __name__ == '__main__':
    app.run(debug=True)
