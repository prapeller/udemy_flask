from app_base import db, Puppy

# create
rufus = Puppy('Rufus', 5)
db.session.add(rufus)
db.session.commit()


# read
print(Puppy.query.all())                            #select * form puppies
print(Puppy.query.get(1).name)                      #select name from puppies where id = 1
print(Puppy.query.filter_by(name='Frankie').all())  #select * from puppies where name = 'Frankie'


# update
puppy_1 = Puppy.query.get(1)
puppy_1.age = 10
db.session.add(puppy_1)
db.session.commit()


# delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()