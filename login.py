# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# from PIL import Image, ImageTk
# import main

# def setup_database():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL UNIQUE,
#             password TEXT NOT NULL
#         )
#     ''')
    
#     conn.commit()
#     conn.close()

# setup_database()

# def execute_db_query(query, parameters=()):
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute(query, parameters)
#     conn.commit()
#     conn.close()

# def register_user():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     if username and password:
#         try:
#             execute_db_query('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#             messagebox.showinfo("Success",'User registered successfully!')
#             entry_username.delete(0, tk.END)
#             entry_password.delete(0, tk.END)
#         except sqlite3.IntegrityError:
#             messagebox.showerror('Username already exists. Please choose a different username.')
#     else:
#         messagebox.showerror('Please fill all fields.')

# def login_user():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     if username and password:
#         user = fetch_db_query('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#         if user:
#             messagebox.showinfo('success','Login successful!')
            
#         else:
#             messagebox.showerror('unsuccessful','Invalid username or password.')
#     else:
#         messagebox.showerror('.','Please fill all fields.')

# def fetch_db_query(query, parameters=()):
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute(query, parameters)
#     record = cursor.fetchone()
#     conn.close()
#     return record

# def login_page():
#     clear_window()
    
#     global login_photo  # Declare the variable as global before using it
    
#     login_img = Image.open("icons/code/loginpageee.png")
    
#     login_img = login_img.resize((1000, 645))
#     login_photo = ImageTk.PhotoImage(login_img)
    
#     tk.Label(root, image=login_photo).place(x=0, y=0)
#     #tk.Label(root, text="Login", font=('Helvetica', 18)).pack(pady=20)
    
#     global entry_username
#     global entry_password
    
#     tk.Label(root, text="Username", font='10',bg='#c5ffb3').place(x=650, y=320)
#     entry_username = tk.Entry(root, width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
#     entry_username.place(x=650, y= 350)
    
#     tk.Label(root, text="Password", font='10',bg='#c5ffb3').place(x=650, y=375)
#     entry_password = tk.Entry(root, show="*", width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
#     entry_password.place(x=650, y=410)
    
#     tk.Button(root, text="Login",font=('comic sans', '10', 'normal'),width='10',bg='lightblue', command=login_user).place(x=700, y=450)
#     tk.Button(root, text="Sign Up",font=('comic sans', '10', 'underline', ),width='10',bg='lightblue', command=signup_page).place(x=800, y=600)

# def signup_page():
#     clear_window()
    
#     global signup_photo  # Declare the variable as global before using it
    
#     signup_img = Image.open("icons/code/registerfinal.png")
#     signup_img = signup_img.resize((1000, 900))
#     signup_photo = ImageTk.PhotoImage(signup_img)
    
#     tk.Label(root, image=signup_photo).place(x=0, y=0)
#     #tk.Label(root, text="Sign Up", font=('Helvetica', 18)).pack(pady=20)
    
#     global entry_username
#     global entry_password
    
#     tk.Label(root, text="Username", font='10',bg='#c5ffb3').place(x=650, y=320)
#     entry_username = tk.Entry(root, width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
#     entry_username.place(x=650, y= 350)
    
#     tk.Label(root, text="Password", font='10',bg='#c5ffb3').place(x=650, y=375)
#     entry_password = tk.Entry(root, show="*", width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
#     entry_password.place(x=650, y=410)
    
#     tk.Button(root, text="Sign Up", font=('comic sans', '10', 'normal'),width='10',bg='skyblue',command=register_user).place(x=680, y=450)
#     tk.Button(root, text="Return to Login", font=('comic sans', '10', 'normal'),width='20',bg='skyblue', command=login_page).place(x=650, y=500)
    

# def clear_window():
#     for widget in root.winfo_children():
#         widget.destroy()

# root = tk.Tk()
# root.title("Login and Sign Up")
# root.geometry('1000x650+250+100')
# root.resizable(False,False)
# root.config(bg= '#66fc03')
# login_page()

# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import main  # Ensure this import matches the location of your main script

def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

setup_database()

def execute_db_query(query, parameters=()):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    conn.commit()
    conn.close()

def register_user():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        try:
            execute_db_query('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            messagebox.showinfo("Success",'User registered successfully!')
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror('Username already exists. Please choose a different username.')
    else:
        messagebox.showerror('Please fill all fields.')

def login_user():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        user = fetch_db_query('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        if user:
            messagebox.showinfo('Success', 'Login successful!')
            
            # Destroy the login window
            root.destroy()
            
            # Create and show the main window
            main_root =tk.Tk()
            app = main.Main(main_root)
            main_root.title("Library Management System...")
            main_root.geometry("1000x650+250+100")
            main_root.iconbitmap('icons/library.ico')
            main_root.resizable(False, False)
            main_root.mainloop()
        else:
            messagebox.showerror('Unsuccessful', 'Invalid username or password.')
    else:
        messagebox.showerror('Error', 'Please fill all fields.')

def fetch_db_query(query, parameters=()):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    record = cursor.fetchone()
    conn.close()
    return record

def login_page():
    clear_window()
    
    global login_photo  # Declare the variable as global before using it
    
    login_img = Image.open("icons/code/loginpageee.png")
    login_img = login_img.resize((1000, 645))
    login_photo = ImageTk.PhotoImage(login_img)
    
    tk.Label(root, image=login_photo).place(x=0, y=0)
    
    global entry_username
    global entry_password
    
    tk.Label(root, text="Username", font='10',bg='#c5ffb3').place(x=650, y=320)
    entry_username = tk.Entry(root, width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
    entry_username.place(x=650, y= 350)
    
    tk.Label(root, text="Password", font='10',bg='#c5ffb3').place(x=650, y=375)
    entry_password = tk.Entry(root, show="*", width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
    entry_password.place(x=650, y=410)
    
    tk.Button(root, text="Login",font=('comic sans', '10', 'normal'),width='10',bg='lightblue', command=login_user).place(x=700, y=450)
    tk.Button(root, text="Sign Up",font=('comic sans', '10', 'underline', ),width='10',bg='lightblue', command=signup_page).place(x=800, y=600)

def signup_page():
    clear_window()
    
    global signup_photo  # Declare the variable as global before using it
    
    signup_img = Image.open("icons/code/registerfinal.png")
    signup_img = signup_img.resize((1000, 900))
    signup_photo = ImageTk.PhotoImage(signup_img)
    
    tk.Label(root, image=signup_photo).place(x=0, y=0)
    
    global entry_username
    global entry_password
    
    tk.Label(root, text="Username", font='10',bg='#c5ffb3').place(x=650, y=320)
    entry_username = tk.Entry(root, width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
    entry_username.place(x=650, y= 350)
    
    tk.Label(root, text="Password", font='10',bg='#c5ffb3').place(x=650, y=375)
    entry_password = tk.Entry(root, show="*", width=20, font=('comic sans', '15', 'normal') , bg='#ffffff')
    entry_password.place(x=650, y=410)
    
    tk.Button(root, text="Sign Up", font=('comic sans', '10', 'normal'),width='10',bg='skyblue',command=register_user).place(x=680, y=450)
    tk.Button(root, text="Return to Login", font=('comic sans', '10', 'normal'),width='20',bg='skyblue', command=login_page).place(x=650, y=500)
    

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Login and Sign Up")
root.geometry('1000x650+250+100')
root.resizable(False,False)
root.config(bg= '#66fc03')
login_page()

root.mainloop()
