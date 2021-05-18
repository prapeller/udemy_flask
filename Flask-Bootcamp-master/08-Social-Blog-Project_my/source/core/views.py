from flask import render_template, request, Blueprint
from source.models import BlogPost

core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html',blog_posts=blog_posts)


@core_blueprint.route('/info')
def info():
    return render_template('info.html')
