from tkinter import *
from functools import partial

def valid(email, password):
	print("email entered :", email.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Password-Saver Form')

#email label and email entry box
emailLabel = Label(tkWindow,text="Email").grid(row=1, column=0)  
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email, show='*').grid(row=1, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)  


validateLogin = partial(valid,email, password)

loginButton = Button(tkWindow, text="Submit", command=valid).grid(row=4, column=0)  

tkWindow.mainloop()
