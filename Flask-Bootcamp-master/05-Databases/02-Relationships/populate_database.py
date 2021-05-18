from models import db, Puppy, Owner, Toy

# Create 2 puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

# Grab Rufus from database, and Create an owner and some Toys to Rufus
rufus = Puppy.query.filter_by(name='Rufus').first() # all()[0]
print(rufus)

jose = Owner("Jose", rufus.id)
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy("Ball", rufus.id)
db.session.add_all([jose, toy1, toy2])
db.session.commit() # Commit these changes to the database

# Let's now grab rufus again after these additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Show toys
print(rufus.report_toys())

# You can also delete things from the database:
# find_pup = Puppy.query.get(1)
# db.session.delete(find_pup)
# db.session.commit()
