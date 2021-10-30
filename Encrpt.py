import csv
import cryptography
from cryptography.fernet import Fernet
import os.path
import base64
import pandas as pd

def write_key():
    key = Fernet.generate_key()
    with open(os.path.join(table_name,'key.key'), "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(os.path.join(table_name,'key.key'), "rb").read()

table_name = input("Enter Table Name")
choice = input("1. write 2. read 3. query")
if choice == "1":
    os.mkdir(table_name)
    write_key()
    key = load_key()
    f = Fernet(key)
    with open(os.path.join(table_name, 'table'+table_name+'.csv'), 'a', newline='') as detailsFile, open('unencrypted'+table_name+'.csv','a') as unFile:
        detailsFileWriter = csv.writer(detailsFile)
        unFileWriter = csv.writer(unFile)
        if os.stat(os.path.join(table_name, 'table'+table_name+'.csv')).st_size == 0:
            detailsFileWriter.writerow(["Name","Surname","Age","Gender"])
        if os.stat('unencrypted'+table_name+'.csv').st_size == 0:
            unFileWriter.writerow(["Name","Surname","Age","Gender"])
        while(True):
            name = input("enter your name:")
            ename = name.encode('utf-8')
            encrypted_name = f.encrypt(ename)
            if(ename == "quit".encode()):
                exit()
            surname = input("enter your surname:")
            esurname = surname.encode('utf-8')
            encrypted_surname = f.encrypt(esurname)
            age = input("enter your age:")
            eage = age.encode('utf-8')
            encrypted_age = f.encrypt(eage)
            gender = input("enter your gender:")
            egender = gender.encode('utf-8')
            encrypted_gender = f.encrypt(egender)

            detailsFileWriter.writerow([encrypted_name,encrypted_surname,encrypted_age,encrypted_gender])
            unFileWriter.writerow([name,surname,age,gender])

        detailsFile.close()
        unFile.close()

elif choice == "2":

    cols = set(map(str, input("Enter the fields which you want to display\n").split(', ')))
    data = pd.read_csv ('unencrypted'+table_name+'.csv')   
    df = pd.DataFrame(data, columns= cols)
    print (df)
    '''key = open(os.path.join(table_name,'key.key'), "rb").read()
    f = Fernet(key)
    with open(os.path.join(table_name, 'table'+table_name+'.csv'), "rb") as files:
        encrypted_data = files.read()
        decrypted_data = (f.decrypt(encrypted_data, 24*60*60))
        print(decrypted_data)
    with open(os.path.join(table_name, 'Result'+table_name+'.csv'), "wb") as files1:
        files1.write(decrypted_data) '''

elif choice == "3":
    query = input("Enter the query")
    if(query == "select * from"+table_name):


