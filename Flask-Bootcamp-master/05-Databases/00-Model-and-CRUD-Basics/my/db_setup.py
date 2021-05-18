from app_base import db, Puppy

# create tables (Model -> table)
db.create_all()

# db.session.add_all([sam, frank])
sam = Puppy('Sammy', 3)
db.session.add(sam)

frank = Puppy('Franky', 4)
db.session.add(frank)

db.session.commit()