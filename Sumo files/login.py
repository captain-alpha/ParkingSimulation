import tkinter as tk
from tkinter import Button, Canvas, Frame, Label, PhotoImage, messagebox
import json
import subprocess
import os

def register():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password.")
    elif username in users:
        messagebox.showerror("Error", "Username already exists. Try a different one.")
    else:
        users[username] = password
        save_users_to_file()
        messagebox.showinfo("Success", "Registration successful.")

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password.")
    elif username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful.")
        launch_app()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def save_users_to_file():
    with open('users.json', 'w') as file:
        json.dump(users, file)

def load_users_from_file():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def launch_appp():
    app_path = 'C:\\Program Files (x86)\\Eclipse\\Sumo\\tools\\osmWebWizard.py'
    subprocess.call(['python', app_path])
    exit()

def launch_app():
    app_path = 'C:\\Users\\abdul\\Desktop\\Sumo files\\Parking Simulation\\osm.sumocfg'
    os.startfile(app_path)
    exit()
    
root = tk.Tk()
root.title("Park Finder Login")
root.geometry("925x500+300+200")
#166b2d
root.configure(bg="#fff")
root.resizable(False,False)
img = PhotoImage(file='C:\\Users\\abdul\\Desktop\\Sumo files\\images\\login.png')
Label(root,image=img,bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x= 480, y=50)

heading = Label(frame, text='Sign in', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)


#bg = PhotoImage(file = "C:\\Users\\abdul\\Pictures\\basic2dMap.png") 
#canvas1 = Canvas( root, width = 400, height = 400) 
#canvas1.pack(fill = "both", expand = True) 
#canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

users = load_users_from_file()

# Center the elements
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")

entry_username = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
entry_username.place(x=30, y=80)
entry_username.insert(0,'Username')
Frame(frame,width=250, height=2, bg='black').place(x=25, y=107)

entry_password = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'), show="*")
entry_password.place(x=30, y=150)
entry_password.insert(0,'Password')
Frame(frame,width=250, height=2, bg='black').place(x=25, y=177)

Button(frame, width=35, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=login).place(x=25, y=215)
label = Label(frame, text="Don't have an account?", fg='black',bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=35, y=270)
#Button(frame, width=35, pady=7, text='Settings', bg='#57a1f8', fg='white', border=0, command=launch_appp).place(x=100, y=215)

sign_up = Button(frame, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=register)
sign_up.place(x=185, y=270)

settings = Button(frame, text='Settings', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=launch_appp)
settings.place(x=275, y=270)


'''
#entry_password = tk.Entry(root, show="*")
button_register = tk.Button(root, text="Register", command=register)
button_login = tk.Button(root, text="Login", command=login)
'''

'''
label_username.grid(row=0, column=0, sticky=tk.E, padx=(5, 0))
label_password.grid(row=1, column=0, sticky=tk.E, padx=(5, 0))
entry_username.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W+tk.E)
entry_password.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W+tk.E)
button_register.grid(row=2, column=0, columnspan=2, pady=5)
button_login.grid(row=3, column=0, columnspan=2, pady=5)
'''


root.mainloop()