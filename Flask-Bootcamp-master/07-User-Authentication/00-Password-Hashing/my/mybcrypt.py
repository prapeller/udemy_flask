from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
passw = 'supersecretpassword'
hashed_pass = bcrypt.generate_password_hash(passw)
print(hashed_pass)

check_1 = bcrypt.check_password_hash(hashed_pass, 'supersecretpass')
print(check_1)

check_2 = bcrypt.check_password_hash(hashed_pass, 'supersecretpassword')
print(check_2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('supersecretpassword')
print(hashed_pass)

print(check_password_hash(hashed_pass, 'wrong'))
print(check_password_hash(hashed_pass, 'supersecretpassword'))