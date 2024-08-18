from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()


class AddBook(Toplevel):
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry("650x580+500+200")
    self.title("Add Book")
    self.resizable(FALSE,False)
    
    ##############Frames_______
    
    #TOP Frame---
    self.topFrame=Frame(self,height=150,bg='white')
    self.topFrame.pack(fill=X)
    
    ##BOTTOM FRAME-----
    self.bottomFrame=Frame(self,height=600,bg='#020875')
    self.bottomFrame.pack(fill=X)
    
    #heading,image
    self.top_image=PhotoImage(file='icons/code/addbook.png')
    top_imag_lbl=Label(self.topFrame,image=self.top_image,bg='white')
    top_imag_lbl.place(x=120,y=10)
    heading = Label(self.topFrame,text=' Add Book ',font='arial 22 bold',fg='#003f8a',bg='white')
    heading.place(x=290,y=60)
    
    ##Entry and labelss_______
    
    #bookName---
    
    self.lbl_name=Label(self.bottomFrame,text="Book:",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_name.place(x=40,y=40)
    self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_name.insert(0,'Enter Book Name')
    self.ent_name.place(x=150,y=45)
    
    #Book Authorr-----
    
    self.lbl_author=Label(self.bottomFrame,text="Author:",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_author.place(x=40,y=80)
    self.ent_author=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_author.insert(0,'Enter Author Name')
    self.ent_author.place(x=150,y=85)
    
    ##Page-----
    self.lbl_page=Label(self.bottomFrame,text="Page :",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_page.place(x=40,y=120)
    self.ent_page=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_page.insert(0,'Enter Page No')
    self.ent_page.place(x=150,y=125)
    
    ##Language-------
    self.lbl_language=Label(self.bottomFrame,text="Language :",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_language.place(x=40,y=160)
    self.ent_language=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_language.insert(0,'Enter Preffered Language')
    self.ent_language.place(x=150,y=165)
    
    ##Buttonn---------
    btn=Button(self.bottomFrame,text='Add Book',command=self.addBook)
    btn.place(x=270,y=200)
    
  def addBook(self):
    name=self.ent_name.get().strip()
    author=self.ent_author.get().strip()
    page=self.ent_page.get().strip()
    language=self.ent_language.get().strip()
    
    if name and author and page and language :
      try:
        query = "INSERT INTO 'books'(book_name,book_author,book_page,book_language) VALUES(?,?,?,?) "
        cur.execute (query,(name,author,page,language))
        con.commit()
        messagebox.showinfo("success","successfully added to data base!",icon='info')
        self.refresh()  
        self.destroy()
        
      
      except sqlite3.Error as e:
        messagebox.showerror("Error","can't add to data base",icon='warning')

    else :
        messagebox.showerror("Error","Fields cant be empty",icon='warning')
    
    
    
    
  
    

    
    