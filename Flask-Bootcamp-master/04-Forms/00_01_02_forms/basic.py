from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField, TextAreaField, \
    SubmitField

from wtforms.validators import DataRequired

site = Flask(__name__)

site.config['SECRET_KEY'] = 'mykey'


class LessonForm(FlaskForm):
    lesson_name = StringField('enter lesson name', validators=[DataRequired()])
    is_published = BooleanField('publish?')
    task_type = RadioField('task type: ', choices=[('type_1', '1_word_image'), ('type_2', '2_word_char_from_lang')])
    active_words = SelectField(u'pick a word: ', choices=[('wo', 'я'), ('ni', 'ты'), ('shi', 'есть')])
    feedsmack = TextAreaField()
    submit = SubmitField('create')


@site.route('/', methods=['GET', 'POST'])
def index():
    lesson_form = LessonForm()
    if lesson_form.validate_on_submit():
        session['lesson_name'] = lesson_form.lesson_name.data
        session['is_published'] = lesson_form.is_published.data
        session['task_type'] = lesson_form.task_type.data
        session['active_words'] = lesson_form.active_words.data
        session['feedback'] = lesson_form.feedsmack.data

        return redirect(url_for('lesson'))

    return render_template('index.html', form=lesson_form)


@site.route('/lesson')
def lesson():
    return render_template('lesson.html')


if __name__ == '__main__':
    site.run(debug=True)
