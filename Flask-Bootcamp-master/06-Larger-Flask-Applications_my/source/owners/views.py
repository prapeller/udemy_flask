from flask import Blueprint, redirect, url_for, render_template
from source.owners.forms import AddForm
from source.models import Owner
from source import db

owners_blueprint = Blueprint('owners',
                             __name__,
                             template_folder='templates/owners')


@owners_blueprint.route('/add_owner', methods=['get', 'post'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('owners.list_owners'))

    return render_template('add_owner.html', form=form)


@owners_blueprint.route('/list_owners', methods=['get', 'post'])
def list_owners():
    owners_list = Owner.query.all()
    return render_template('list_owners.html', owners_list=owners_list)
