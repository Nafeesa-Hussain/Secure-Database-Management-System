import csv
import cryptography
from cryptography.fernet import Fernet
import os.path

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

write_key()

key = load_key()
f = Fernet(key)

table_name = input("Enter Table Name")

f = Fernet(key)
with open('table'+table_name+'.csv', "rb") as files:
    encrypted_data = files.read()
    decrypted_data = f.decrypt(encrypted_data)
with open('Result'+table_name+'.csv', "wb") as files1:
    files1.write(decrypted_data)   ''' 

