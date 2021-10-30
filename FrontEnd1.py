from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import pymysql #pip install pymysql
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii
import csv
import os.path

class Frontend:
    def __init__(self,root):
        self.root=root
        self.root.title("SDBMS")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg=ImageTk.PhotoImage(file='bg.jpg')
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file='smallbg.jpg')
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(bg,text="One Step to Save your Data",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=600,y=30)

        table1=Label(frame1,text="Table1 Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=30)
        self.txt_table1=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_table1.place(x=50,y=60,width=250)

        table2=Label(frame1,text="Table2 Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=30)
        self.txt_table2=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_table2.place(x=370,y=60,width=250)
        
        name=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=50,y=130,width=250)

        dept_name=Label(frame1,text=" Department Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
        self.txt_dept_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_dept_name.place(x=50,y=210,width=250)

        id1=Label(frame1,text="ID",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=180)
        self.txt_id1=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_id1.place(x=370,y=210,width=250)

        salary=Label(frame1,text="Salary",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
        self.txt_salary=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_salary.place(x=50,y=290,width=250)
        
        branch_name=Label(frame1,text="Branch Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=260)
        self.txt_branch_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_branch_name.place(x=370,y=290,width=250)

        Choice=Label(frame1,text="Operation",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Write","Read","Join","Query","Create")
        self.cmb_quest.place(x=370,y=130,width=250)
        self.cmb_quest.current(0)
        
        Query = Label(frame1,text="Write your Query Here",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=350)
        self.txt_query=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_query.place(x=370,y=380,width=250)

        dept_id = Label(frame1,text="Department ID",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=350)
        self.txt_dept_id=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_dept_id.place(x=50,y=380,width=250)

        self.btn_img=ImageTk.PhotoImage(file="submit.png")
        btn = Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.submit).place(x=290,y=420,width=120,height=50)

    

    def clear(self):
        self.txt_name.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_query.delete(0,END)
        self.txt_dept_id.delete(0,END)
        self.txt_branch_name.delete(0,END)
        self.txt_salary.delete(0,END)
        self.txt_dept_name.delete(0,END)
        self.txt_id1.delete(0,END)

    def submit(self):

       keyPair = RSA.generate(3072)
       pubKey = keyPair.publickey()
       pubKeyPEM = pubKey.exportKey()
       privKeyPEM = keyPair.exportKey()

       var_query = self.txt_query.get()
       var_operation = self.cmb_quest.get()
       var_table1 = self.txt_table1.get()
       var_table2 = self.txt_table2.get()
       
       var_name = self.txt_name.get()
       name_msg = bytes(str(var_name), 'utf-8')
       name_encryptor = PKCS1_OAEP.new(pubKey)
       name_encrypted = name_encryptor.encrypt(name_msg)
       
       var_dept_name = (self.txt_dept_name.get())
       dept_name_msg = bytes(str(var_dept_name), 'utf-8')
       dept_name_encryptor = PKCS1_OAEP.new(pubKey)
       dept_name_encrypted = dept_name_encryptor.encrypt(name_msg)

       var_id1 = (self.txt_id1.get())
       id1_msg = bytes(str(var_id1), 'utf-8')
       id1_encryptor = PKCS1_OAEP.new(pubKey)
       id1_encrypted = id1_encryptor.encrypt(id1_msg)

       var_salary = self.txt_salary.get()
       salary_msg = bytes(str(var_salary), 'utf-8')
       salary_encryptor = PKCS1_OAEP.new(pubKey)
       salary_encrypted = salary_encryptor.encrypt(salary_msg)

       var_branch_name = (self.txt_branch_name.get())
       branch_name_msg = bytes(str(var_branch_name), 'utf-8')
       branch_name_encryptor = PKCS1_OAEP.new(pubKey)
       branch_name_encrypted = branch_name_encryptor.encrypt(branch_name_msg)

       var_dept_id = (self.txt_dept_id.get())
       dept_id_msg = bytes(str(var_dept_id), 'utf-8')
       dept_id_encryptor = PKCS1_OAEP.new(pubKey)
       dept_id_encrypted = dept_id_encryptor.encrypt(dept_id_msg)

       name_decryptor = PKCS1_OAEP.new(keyPair)
       name_decrypted = name_decryptor.decrypt(name_encrypted)
       #print('Decrypted:', name_decrypted.decode('utf-8'))

       id1_decryptor = PKCS1_OAEP.new(keyPair)
       id1_decrypted = id1_decryptor.decrypt(id1_encrypted)
      # print('Decrypted:', id1_decrypted.decode('utf-8'))
       
       dept_name_decryptor = PKCS1_OAEP.new(keyPair)
       dept_name_decrypted = dept_name_decryptor.decrypt(dept_name_encrypted)
       #print('Decrypted:', dept_name_decrypted.decode('utf-8'))

       try:
            con= pymysql.connect(host="localhost",user="root",password="123456@abc",database="anz")
            con1= pymysql.connect(host="localhost",user="root",password="123456@abc",database="database2")
            cur = con.cursor()
            cur1 = con1.cursor()
            if (self.cmb_quest.get() == "Read"):
                cur1.execute(var_query)
                records = cur1.fetchall()
                print(records)

            elif(self.cmb_quest.get() == "Create"):
                cur.execute(var_query)
            
            elif(self.cmb_quest.get()=="Write" and self.txt_table2.get()!=""):
                cur.execute("insert into anz.departments(dept_id,dept_name) values(%s,%s)",(dept_id_encrypted,dept_name_encrypted))
                cur1.execute("insert into database2.departments(dept_id,dept_name) values(%s,%s)",(var_dept_id,var_dept_name))
                self.keyStore(var_dept_id,keyPair)
                cur.execute("insert into anz.employees(name,dept_id,id,salary,branch_name) values(%s,%s,%s,%s,%s)", (name_encrypted,dept_id_encrypted,id1_encrypted,salary_encrypted,branch_name_encrypted) )
                cur1.execute("insert into database2.employees(name,dept_id,id,salary,branch_name) values(%s,%s,%s,%s,%s)", (var_name,var_dept_id,var_id1,var_salary,var_branch_name) )
                self.keyStore(var_id1,keyPair)

            elif(self.cmb_quest.get() == "Write" and self.txt_dept_name.get() != ""):
                cur.execute("insert into anz.departments(dept_id,dept_name) values(%s,%s)",(dept_id_encrypted,dept_name_encrypted))
                cur1.execute("insert into database2.departments(dept_id,dept_name) values(%s,%s)",(var_dept_id,var_dept_name))
                self.keyStore(var_dept_id,keyPair)

            elif(self.cmb_quest.get() == "Write"):
                cur.execute("insert into anz.employees(name,dept_id,id,salary,branch_name) values(%s,%s,%s,%s,%s)", (name_encrypted,dept_id_encrypted,id1_encrypted,salary_encrypted,branch_name_encrypted) )
                cur1.execute("insert into database2.employees(name,dept_id,id,salary,branch_name) values(%s,%s,%s,%s,%s)", (var_name,var_dept_id,var_id1,var_salary,var_branch_name) )         
                self.keyStore(var_id1,keyPair)
            
            elif(self.cmb_quest.get() == "Join")  :
                cur1.execute(var_query)  #join query
                print("ID    Name    Salary    Dept_Id    Dept_Name")  
                for row in cur1:  
                    print("%d    %s    %d    %s    %s"%(row[0], row[1],row[2],row[3],row[4]))

            elif(self.cmb_quest.get() == "Query") :
                cur1.execute(var_query) #sub query
                sub = cur1.fetchall()
                for row in sub:
                    print(row)

            con.commit()
            con1.commit()
            con.close()
            con1.close()
            messagebox.showinfo("Success","Operation done",parent=self.root)
            self.clear()
       except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def keyStore(self,id2,keyPair):
        with open('keyStore.csv', 'a', newline='') as detailsFile:
            detailsFileWriter = csv.writer(detailsFile)
            detailsFileWriter.writerow([id2,keyPair])
            detailsFile.close()


root=Tk()
obj=Frontend(root)
root.mainloop()





#statement = "SELECT %s FROM %s WHERE %s IN (SELECT %s FROM %s)" %(column, table1, colref, colref, table2)





'''decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted.decode('utf-8'))'''

