from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from source import db
from source.models import User, BlogPost
from source.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from source.users.picture_handler import add_profile_pic

users_blueprint = Blueprint('users', __name__)


# register
@users_blueprint.route('/register', methods=['get', 'post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


# login
@users_blueprint.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cur_user = User.query.filter_by(email=form.email.data).first()
        if cur_user and cur_user.check_password(form.password.data):
            login_user(cur_user)
            flash('login success')

            next = request.args.get('next')
            if next is None or next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)


# logout
@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


# account (update UserForm)
@users_blueprint.route('/account', methods=['get', 'post'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


# user's list of Blog posts
@users_blueprint.route('/<username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)
