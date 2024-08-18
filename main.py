from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
import addbook,addmember,givebook

con = sqlite3.connect('library.db')
cur = con.cursor()

# Creating a class for Main
class Main:
    def __init__(self, master):
        self.master = master
        
        def displayStatictics(event):
            count_books=cur.execute("SELECT count(book_id) FROM books").fetchall()
            count_members=cur.execute("SELECT count(member_id)FROM members").fetchall()
            count_taken_books=cur.execute("SELECT count(book_status)FROM books WHERE book_status=1").fetchall()
            
            self.lbl_book_count.config(text="Total:"+str(count_books[0][0])+'books in library')
            self.lbl_member_count.config(text="Total member : "+str(count_members[0][0]))
            self.lbl_taken_count.config(text="Taken books :"+str(count_taken_books[0][0]))
            displayBooks(self)
        
        
        
        def displayBooks(self):
            books =cur.execute('select * FROM books').fetchall()
            count = 0
            self.list_books.delete(0,END)
            
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0])+ "-" +book[1])
                count+=1
            def bookInfo(event):
                try:
                    value = str(self.list_books.get(self.list_books.curselection()))
                    id=value.split("-")[0]
                    book = cur.execute("SELECT * FROM books WHERE book_id=?",(id,))
                    book_info=book.fetchall()
                    print(book_info)
                    self.list_details.delete(0,END)
                    self.list_details.insert(0,"Book Name :"+book_info[0][1])
                    self.list_details.insert(1,"Author :"+book_info[0][2])
                    self.list_details.insert(2,"Page :"+book_info[0][3])
                    self.list_details.insert(3,"Language :"+book_info[0][4])
                    if book_info[0][5] == 0:
                        self.list_details.insert(4,"Status : Available")
                    else:
                        self.list_details.insert(4,"Status : Not Available!")
                except TclError:
                    pass
            
                    
            def doubleClick(event):
                global given_id 
                value=str(self.list_books.get(self.list_books.curselection()))
                given_id=value.split("-")[0]
                give_book=EditBook(self)   
         
                
            self.list_books.bind('<<ListboxSelect>>',bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>',displayStatictics)
            self.list_books.bind('<Double-Button-1>',doubleClick)
            
      
        
            
    # Frames
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Top side frame
        topFrame = Frame(mainFrame, width=1000, height=70, bg='#e6e5e1', padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill='x')

        # Center frame
        centerFrame = Frame(mainFrame, width=1000, relief=RIDGE, bg='#88b8b4', height=600)
        centerFrame.pack(side=TOP)

        # Center left side Frame
        centerLeftFrame = Frame(centerFrame, width=600, height=600, bg='#1a1563', borderwidth=2, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT, fill=BOTH, expand=True)

        # Center right side Frame
        centerRightFrame = Frame(centerFrame, width=400, height=600, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Search bar
        search_bar = LabelFrame(centerRightFrame, width=390, height=100, text="Search Box", bg='#9bc9ff')
        search_bar.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        self.lbl_search = Label(search_bar, text='Search:', font=('arial', 12, 'bold'), bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=10, pady=5)

        # Entry box
        self.ent_search = Entry(search_bar, width=20, bd=5)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

        self.btn_search = Button(search_bar, text='Search', font=('arial', 12, 'bold'), bg='#fcc324', fg='white', activebackground='#fcc324', activeforeground='white',command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=10, pady=5)

        # List Bar
        list_bar = LabelFrame(centerRightFrame, width=390, height=100, text='List Box', bg='#fcc324')
        list_bar.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        lbl_list = Label(list_bar, text='Sort by:', font='times 14 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=1)

        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text="All Books", variable=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='Available', variable=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text="Borrowed Books", variable=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)

        # Listbook Button
        btn_list = Button(list_bar, text='List Books', bg='#2488ff', fg='white', font='arial 12', activebackground='#2488ff', activeforeground='white',command=self.listBooks)
        btn_list.grid(row=1, column=3, padx=20, pady=5)

        ###################### TOOL BAR ###################

        # Title and Image
        image_bar = Frame(centerRightFrame, width=390, height=250)
        image_bar.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        self.title_right = Label(image_bar, text='Welcome to Library', font='arial 14 bold')
        self.title_right.grid(row=0, pady=(10, 0))

        self.image_library = Image.open('icons/code/Untitled.png')
        self.image_library = self.image_library.resize((390, 200), Image.LANCZOS)
        self.image_library = ImageTk.PhotoImage(self.image_library)

        self.lbl_Image = Label(image_bar, image=self.image_library)
        self.lbl_Image.grid(row=1, pady=(5, 0), sticky='n')

        ################Tabs...##################
        ##TAB--1
        self.tabs = ttk.Notebook(centerLeftFrame, width=600, height=600)
        self.tabs.pack()
        self.tab1_icon = Image.open('icons/code/Books.png').resize((30, 30), Image.LANCZOS)
        self.tab1_icon = ImageTk.PhotoImage(self.tab1_icon)
        self.tab2_icon = Image.open('icons/code/statistic.png').resize((30, 30), Image.LANCZOS)
        self.tab2_icon = ImageTk.PhotoImage(self.tab2_icon)
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)

        # Standard icon size
        icon_size = (25, 25)

        ##list books
        self.list_books = Listbox(self.tab1, width=30, height=20, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky='n')
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N + S + E)

        ##LIST details
        self.list_details = Listbox(self.tab1, width=60, height=20, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        ##TAB--2
        #statistics
        self.lbl_book_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # Add Book
        self.iconbook = Image.open('icons/code/addbook.png').resize(icon_size, Image.LANCZOS)
        self.iconbook = ImageTk.PhotoImage(self.iconbook)

        self.btnbook = Button(topFrame, text='Add Book', image=self.iconbook, compound=LEFT, font='Arial 12 bold', command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=10)

        # Add Member button
        self.iconmember = Image.open('icons/addpeople.png').resize(icon_size, Image.LANCZOS)
        self.iconmember = ImageTk.PhotoImage(self.iconmember)

        self.btnAddMember = Button(topFrame, text='Add Member', font='arial 12 bold', padx=10, image=self.iconmember, compound=LEFT,command=self.addMember)
        self.btnAddMember.pack(side=LEFT)

        # Book Given
        self.iconLendbook = Image.open('icons/code/givebook.png').resize(icon_size, Image.LANCZOS)
        self.iconLendbook = ImageTk.PhotoImage(self.iconLendbook)

        self.btnLendBook = Button(topFrame, text="Give Book", font='arial 12 bold', padx=10, image=self.iconLendbook, compound=LEFT,command=self.giveBook)
        self.btnLendBook.pack(side=LEFT)
        
        self.iconLogout = Image.open('icons/code/logout.png').resize(icon_size, Image.LANCZOS)
        self.iconLogout = ImageTk.PhotoImage(self.iconLogout)

        self.btnLogout = Button(topFrame, text="Log Out", font='arial 12 bold', padx=10, image=self.iconLogout, compound=LEFT, command=self.logout)
        self.btnLogout.pack(side=RIGHT, padx=10)
        
        
        
        #funtion call
        displayBooks(self)
        displayStatictics(self)
    def logout(self):
        confirm = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
        if confirm:
            self.master.destroy()
    
    def listBooks(self):
        value = self.listChoice.get()
        if value ==1:
            allbooks=cur.execute("SELECT * FROM BOOKS").fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in allbooks:
               self.list_books.insert(count,str(book[0])+"-"+book[1]) 
               count +=1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status =?",(0,)).fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in books_in_library:
               self.list_books.insert(count,str(book[0])+"-"+book[1]) 
               count +=1
        else:
            borrowed_books=cur.execute("SELECT * FROM books WHERE book_status =?",(1,)).fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in borrowed_books:
               self.list_books.insert(count,str(book[0])+"-"+book[1]) 
               count +=1
            
    def refresh(self):
        books =cur.execute('select * FROM books').fetchall()
        count = 0
        self.list_books.delete(0,END)
        
        for book in books:
            print(book)
            self.list_books.insert(count,str(book[0])+ "-" +book[1])
            count+=1
        def bookInfo(event):
            value = str(self.list_books.get(self.list_books.curselection()))
            id=value.split("-")[0]
            book = cur.execute("SELECT * FROM books WHERE book_id=?",(id,))
            book_info=book.fetchall()
            print(book_info)
            self.list_details.delete(0,END)
            self.list_details.insert(0,"Book Name :"+book_info[0][1])
            self.list_details.insert(1,"Author :"+book_info[0][2])
            self.list_details.insert(2,"Page :"+book_info[0][3])
            self.list_details.insert(3,"Language :"+book_info[0][4])
            if book_info[0][5] == 0:
                self.list_details.insert(4,"Status : Available")
            else:
                self.list_details.insert(4,"Status : Not Available!")
                
        def doubleClick(event):
            global given_id 
            value=str(self.list_books.get(self.list_books.curselection()))
            given_id=value.split("-")[0]
            give_book=EditBook(self)   
        
        
            
        self.list_books.bind('<<ListboxSelect>>',bookInfo)
        # self.tabs.bind('<<NotebookTabChanged>>',displayStatictics)
        self.list_books.bind('<Double-Button-1>',doubleClick)
        
    def addBook(self):
        add = addbook.AddBook()
        
        
        
    def addMember(self):
        member = addmember.AddMember()
        
        
    def searchBooks(self):
        value=self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?",('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count=0
        for book in search:
            self.list_books.insert(count,str(book[0])+"-"+book[1])
            count +=1



    def giveBook(self):
        give_book=givebook.GiveBook()
    

class EditBook(Toplevel):
    def __init__(self, main_instance):
        super().__init__()
        self.main_instance = main_instance
        self.geometry("650x650+350+100")
        self.title("Lend Book")
        self.resizable(False, False)
        
        global given_id
        self.book_id = int(given_id)

        # Querying the database for books and members
        query = "SELECT book_name, book_author FROM books where book_id = ?"
        books = cur.execute(query,(self.book_id,)).fetchall()
        # book_list = [f"{book[0]}-{book[1]}" for book in books]

        query2 = "SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list = [f"{member[0]}-{member[1]}" for member in members]

        # TOP Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        # BOTTOM FRAME
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading and image
        self.top_image = PhotoImage(file='icons/addpeople.png')  # Ensure this file path is correct
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)

        heading = Label(self.topFrame, text='Lend Book', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=300, y=100)

        # Book dropdown
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text="Book:", font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        
        self.lbl_Bookname=Label(self.bottomFrame,text="Book :",font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_Bookname.place(x=40,y=40)
        self.ent_Bookname=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_Bookname.delete(0,END)
        self.ent_Bookname.insert(0,str(books[0][0]))
        self.ent_Bookname.place(x=150,y=45)
    
        self.lbl_BookAuthor=Label(self.bottomFrame,text="Author:",font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_BookAuthor.place(x=40,y=80)
        self.ent_BookAuthor=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_BookAuthor.delete(0,END)
        self.ent_BookAuthor.insert(0,str(books[0][1]))
        self.ent_BookAuthor.place(x=150,y=85)
    
    


        # Lend Book button
        btn = Button(self.bottomFrame, text='Update', command=self.updateBook)
        btn.place(x=228, y=120)
        
        btn = Button(self.bottomFrame, text='Delete', command=self.deleteBook)
        btn.place(x=328, y=120)
        
    def deleteBook(self):
        if given_id:
            try:
                cur.execute("DELETE FROM books WHERE book_id=?", (given_id,))
                con.commit()
                messagebox.showinfo("Success", "Book has been successfully deleted!", icon='info')
                self.main_instance.refresh()  # Refresh the book list
                EditBook.destroy(self)
            except Exception as e:
                messagebox.showerror("Error", str(e), icon='warning')
        else:
            messagebox.showerror("Error", "Book cannot be found", icon='warning')
    def updateBook(self):
        # book_id = self.book_name.get().split('-')[0]
        # member_id = self.member_name.get().split('-')[0]
        
        addedBookName = self.ent_Bookname.get()
        addedBookAuthor= self.ent_BookAuthor.get()

        if addedBookName and addedBookAuthor:
            try:
                cur.execute("UPDATE books SET book_name=?, book_author=? WHERE book_id=?", (addedBookName,addedBookAuthor,given_id,))
                con.commit()
                messagebox.showinfo("Success", "Book has been successfully updated!", icon='info')
                self.main_instance.refresh()  # Refresh the book list
                
                EditBook.destroy(self)
            except Exception as e:
                messagebox.showerror("Error", str(e), icon='warning')
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon='warning')

        
def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System...")
    root.geometry("1000x650+250+100")
    root.iconbitmap('icons/library.ico')
    root.resizable(FALSE,False)
    root.mainloop()

if __name__ == '__main__':
    main()


