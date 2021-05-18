from source import app, db
from source.models import User
from source.forms import LoginForm, RegistrationForm
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_required, login_user, logout_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logged out!')
    return redirect(url_for('index'))


@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!')

            next = request.args.get('next')
            # <-- usually request.args.get('next') is None,
            # it is not None if user trying to access to some @login_required view

            if next is None or next[0] != '/':  # <-- if user went directly to login or not at index page
                next = url_for('welcome_user')  # <-- next = 'welcome_user'

            return redirect(next)  # send user to 'welcome_user'

        if user is not None and not user.check_password(form.password.data):
            flash('wrong password')

        if user is None:
            flash('Not registered user!')

    return render_template('login.html', form=form)


@app.route('/register', methods=['get', 'post'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
