from cryptography.fernet import Fernet
# read the key
with open('file_key.key', 'rb') as filekey:
    key = filekey.read()
# crate instance of Fernet
# with encryption key
fernet = Fernet(key)
# read the file to decrypt
with open('maddy.txt', 'rb') as f:
    file = f.read()

# decrypt the file
decrypt_file = fernet.decrypt(file)
# open the file and wite the encrypted data
with open('maddy.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypt_file)
