from fileinput import filename
from tkinter import *
from cryptography.fernet import Fernet
import subprocess as sp
global name1, passw_var,filename1
#program for interface to registartion
a = ""
b = ""

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

name_var = StringVar()

f = ('Times', 14)
var = StringVar()
var.set('male')

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Create notepad",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)


register_name = Entry(

    right_frame,
    textvariable=name_var,
    font=f
)

create_btn = Button(
    right_frame,
    width=15,
    text='Create notepad',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: create_function()
)


open_btn = Button(
    right_frame,
    width=15,
    text='open file',
    font=f,
    relief=SOLID,
    cursor='hand2',
    #command=lambda: open_function(name_var, passw_var)
)

encode_btn = Button(
    right_frame,
    width=15,
    text='ENCODE',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: encode_function()
)
decode_btn = Button(
    right_frame,
    width=15,
    text='DECODE',
    font=f,
    relief=SOLID,
    cursor='hand2',
    #command=lambda: decode_function(name_var, passw_var)
)

def create_function():
    file_name=name_var.get()
    programname = "notepad.exe"
    print(file_name)
    filename = file_name
    filename1 = filename + ".txt"
    print(filename1)
    sp.Popen([programname, filename], stdout=sp.PIPE, stderr=sp.STDOUT,
             shell=(True, False))    # pylint: disable=protected-access
    return filename1


def encode_function():
        # generate encryption key
        file_name5 = name_var.get()
        filename4 = file_name5 + ".txt"
        print(filename4)
        key = Fernet.generate_key()
        # write the key in a file of .key extension
        with open('file_key.key', 'wb') as filekey:
            filekey.write(key)
        # crate instance of Fernet
        # and load generated key
        fernet = Fernet(key)
        # read the file to encrypt
        with open(filename4, 'rb') as f:
            file = f.read()
    # encrypt the file
        encrypt_file = fernet.encrypt(file)
        # open the file and wite the encryption data
        with open(filename4, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
        print('File is encrypted')


register_name.grid(row=0, column=1, pady=10, padx=30)


encode_btn.grid(row=8, column=0, pady=10, padx=20)
decode_btn.grid(row=8, column=1, pady=10, padx=20)

create_btn.grid(row=7, column=1, pady=10, padx=20)
open_btn.grid(row=7, column=0, pady=10, padx=20)
right_frame.pack()
ws.mainloop()
