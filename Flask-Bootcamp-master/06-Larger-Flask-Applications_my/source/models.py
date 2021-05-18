from source import db


class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)  # 1-1

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'id: {self.id}, name: {self.name}, owner: {self.owner.name}'
        else:
            return f'id: {self.id}, name: {self.name}, owner: No Owner'


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        if Puppy.query.get(self.puppy_id):
            return f'id: {self.id}, name: {self.name}, puppy: {Puppy.query.get(self.puppy_id).name}'
        else:
            return f'id: {self.id}, name: {self.name}, puppy: No Puppy'

