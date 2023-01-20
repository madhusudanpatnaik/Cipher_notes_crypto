#Retrieve credentials.

from cryptography.fernet import Fernet
import os

cred_filename = 'CredFile.ini'
key_file = 'key.key'

key = ''

with open('key.key', 'r') as key_in:
	key = key_in.read().encode()

#If you want the Cred file to be of one
# time use uncomment the below line

os.remove(key_file)
f = Fernet(key)
with open(cred_filename, 'r') as cred_in:
	lines = cred_in.readlines()
	config = {}
	for line in lines:
		tuples = line.rstrip('\n').split('=', 1)
		if tuples[0] in ('Username', 'Password'):
			config[tuples[0]] = tuples[1]

	passwd = f.decrypt(config['Password'].encode()).decode()
	print("Password:", passwd)
user=(config['Username'])
print("User:", user)

