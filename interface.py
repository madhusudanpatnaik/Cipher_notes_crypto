from cgitb import text
from tkinter import *
from atexit import register
from typing import get_args
from unicodedata import name
from cryptography.fernet import Fernet
import re
import ctypes
import time
import os
import sys
from cred_view import *


ws = Tk()
ws.title('CIPHER NOTES')
ws.config(bg='#0B5A81')

name_var2 = StringVar()
password_var2 = StringVar()

f = ('Times', 14)
var = StringVar()
var.set('male')
name_var1 = ""
password_var1 = ""

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
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

register_name = Entry(
    right_frame,
    textvariable=name_var2,
    font=f
)

register_pwd = Entry(
    right_frame,
    textvariable=password_var2,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: callback_function())


login_btn = Button(
    right_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: callback_function2(name_var2, password_var2))


def callback_function():
    print("register")
    ws.destroy()
    import credsavig as cred
    cred.main()


def callback_function2(name_var2, password_var2):
    name2 = name_var2.get()
    password_var2 = password_var2.get()
    if (name2 == user and password_var2 == passwd):
        print("useername")
    else:
        print("login not wokring")

    print("login")
    #do something


register_name.grid(row=0, column=1, pady=10, padx=20)


register_pwd.grid(row=5, column=1, pady=10, padx=20)


login_btn.grid(row=7, column=0, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()
ws.mainloop()
