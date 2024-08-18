from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x580+500+200")
        self.title("Lend Book")
        self.resizable(False, False)
        
        
        

        # Querying the database for books and members
        query = "SELECT * FROM books WHERE book_status=0"
        books = cur.execute(query).fetchall()
        book_list = [f"{book[0]}-{book[1]}" for book in books]

        query2 = "SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list = [f"{member[0]}-{member[1]}" for member in members]

        # TOP Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        # BOTTOM FRAME
        self.bottomFrame = Frame(self, height=500, bg='#020875')
        self.bottomFrame.pack(fill=X)

        # Heading and image
        try:
            self.top_image = PhotoImage(file='icons/addpeople.png')  # Ensure this file path is correct
            top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
            top_image_lbl.place(x=120, y=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            top_image_lbl = Label(self.topFrame, text="Image not found", bg='white')
            top_image_lbl.place(x=120, y=10)

        heading = Label(self.topFrame, text='Lend Book', font='arial 22 bold', fg='#003f8a', bg='#020875')
        heading.place(x=300, y=100)

        # Book dropdown
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text="Book:", font='arial 15 bold', fg='white', bg='#020875')
        self.lbl_name.place(x=40, y=40)

        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.place(x=150, y=45)

        # Member dropdown
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text="Member:", font='arial 15 bold', fg='white', bg='#020875')
        self.lbl_member.place(x=40, y=80)

        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # Lend Book button
        btn = Button(self.bottomFrame, text='Lend Book', command=self.lendBook)
        btn.place(x=228, y=120)

    def lendBook(self):
        book_id = self.book_name.get().split('-')[0]
        member_id = self.member_name.get().split('-')[0]

        if book_id and member_id:
            try:
                cur.execute("UPDATE books SET book_status=1 WHERE book_id=?", (book_id,))
                con.commit()
                messagebox.showinfo("Success", "Book has been lent successfully!", icon='info')
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e), icon='warning')
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon='warning')

