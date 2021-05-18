from flask import Blueprint, redirect, url_for, render_template
from source.puppies.forms import AddForm, DelForm
from source import db
from source.models import Puppy

puppies_blueprint = Blueprint('puppies',
                              __name__,
                              template_folder='templates/puppies')


@puppies_blueprint.route('/add_pup', methods=['get', 'post'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pups'))

    return render_template('add_puppy.html', form=form)


@puppies_blueprint.route('/del_pup', methods=['get','post'])
def delete_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        del_pup = Puppy.query.get(id)
        db.session.delete(del_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pups'))

    return render_template('del_puppies.html', form=form)


@puppies_blueprint.route('/list_pups')
def list_pups():
    puppies_list = Puppy.query.all()
    return render_template('list_puppies.html', puppies_list=puppies_list)
