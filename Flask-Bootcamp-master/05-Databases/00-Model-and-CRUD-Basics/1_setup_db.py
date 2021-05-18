# Import database info
from basic_model import db, Puppy

# Create the tables in the database. (Usually won't do it this way!)
db.create_all()

# Create new entries in the database
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

# Check ids (haven't added sam and frank to database, so they should be None)
print(sam.id)
print(frank.id)

# Ids will get created automatically once we add these entries to the DB
db.session.add_all([sam,frank])

# Alternative for individual additions:
# db.session.add(sam)
# db.session.add(frank)

# Now save it to the database
db.session.commit()

# Check the ids
print(sam.id)
print(frank.id)
