from tkinter import *
global name1,passw_var,password1
#program for interface to registartion

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

name_var = StringVar()
passw_var = StringVar()

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
    textvariable=name_var,
    font=f
)

register_pwd = Entry(
    right_frame,
    textvariable = passw_var,
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
    command=lambda:callback_function(name_var,passw_var)
    )





def callback_function(name_var,passw_var):
    
    global name1,password1
    name1= name_var.get()
    password1 = passw_var.get()
    print(name1)
    name_var.set("")
    passw_var.set("")
    return name1, password1
    
    
    # do something



register_name.grid(row=0, column=1, pady=10, padx=20)


register_pwd.grid(row=5, column=1, pady=10, padx=20)


register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()
ws.mainloop()
