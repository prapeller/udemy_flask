from flask import Blueprint, render_template

err_blueprint = Blueprint('err_pages', __name__)


@err_blueprint.app_errorhandler(404)
def error_404(error):
    return render_template('errors_pages/404.html'), 404


@err_blueprint.app_errorhandler(403)
def error_403(error):
    return render_template('errors_pages/403.html'), 403
