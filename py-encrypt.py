import bcrypt
import getpass

#an hashtable mechanism aka a password generator
password = getpass.getpass("password: ")
print(password)
hash_pw = bcrypt.hashpw(password.encode("utf-8"),
bcrypt.gensalt())
reverse = hash_pw.decode()
#print(reverse)
print(reverse.encode())
