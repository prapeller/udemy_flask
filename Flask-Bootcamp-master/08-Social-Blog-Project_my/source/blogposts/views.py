from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import current_user, login_required
from source import db
from source.models import BlogPost
from source.blogposts.forms import BlogPostForm

blog_posts_blueprint = Blueprint('blog_posts', __name__)


# blog_post (views):
#    create
@blog_posts_blueprint.route('/create', methods=['get', 'post'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(
            title=form.title.data,
            text=form.text.data,
            user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)


#    read
@blog_posts_blueprint.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=blog_post.title,
                           date=blog_post.date, post=blog_post)


#    update
@blog_posts_blueprint.route('/<int:blog_post_id>/update', methods=["GET", "POST"])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post.title = form.title.data,
        blog_post.text = form.text.data,
        db.session.commit()
        flash('Blog Post updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    elif request.method == "GET":
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', title='Updating', form=form)


#    delete
@blog_posts_blueprint.route('/<int:blog_post_id>/delete', methods=['get', 'post'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('blog post deleted')
    return redirect(url_for('core.index'))
