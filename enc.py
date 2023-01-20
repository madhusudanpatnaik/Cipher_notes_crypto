from cryptography.fernet import Fernet

# generate encryption key
key = Fernet.generate_key()
# write the key in a file of .key extension
with open('file_key.key', 'wb') as filekey:
    filekey.write(key)
# crate instance of Fernet
# and load generated key
fernet = Fernet(key)
# read the file to encrypt
with open('maddy.txt', 'rb') as f:
    file = f.read()
    
# encrypt the file
encrypt_file = fernet.encrypt(file)
# open the file and wite the encryption data
with open('maddy.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypt_file)
print('File is encrypted')