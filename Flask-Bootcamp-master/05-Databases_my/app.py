from flask import Flask, render_template, redirect, url_for
from forms import AddPupForm, AddOwnerForm, DelPupForm
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask start
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# db/migrate setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'adopt_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# Models
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'id: {self.id} name: {self.name} owner: {self.owner.name}'
        else:
            return f'id: {self.id} name: {self.name} owner: -'


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'name: {self.name}\tpuppy: {Puppy.query.get(self.puppy_id).name}'


# Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_pup', methods=['post', 'get'])
def add():
    form = AddPupForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('add_pup.html', form=form)


@app.route('/del_pup', methods=['post', 'get'])
def delete():
    form = DelPupForm()
    if form.validate_on_submit():
        id = form.id.data
        del_pup = Puppy.query.get(id)
        db.session.delete(del_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('del_pup.html', form=form)


@app.route('/list_pup')
def list_pup():
    pup_list = Puppy.query.all()
    return render_template('list_pup.html', pup_list=pup_list)


@app.route('/add_own', methods=['post', 'get'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('add_own.html', form=form)


# run
if __name__ == '__main__':
    app.run(debug=True)
