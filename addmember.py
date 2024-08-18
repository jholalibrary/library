from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()


class AddMember(Toplevel):
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry("650x580+500+200")
    self.title("Add Member")
    self.resizable(FALSE,False)
    
    ##############Frames_______
    
    #TOP Frame---
    self.topFrame=Frame(self,height=150,bg='white')
    self.topFrame.pack(fill=X)
    
    ##BOTTOM FRAME-----
    self.bottomFrame=Frame(self,height=600,bg='#020875')
    self.bottomFrame.pack(fill=X)
    
    #heading,image
    self.top_image=PhotoImage(file='icons/addpeople.png')
    top_imag_lbl=Label(self.topFrame,image=self.top_image,bg='white')
    top_imag_lbl.place(x=120,y=10)
    heading = Label(self.topFrame,text=' Add Member ',font='arial 22 bold',fg='#003f8a',bg='white')
    heading.place(x=300,y=100)
    
    ##Entry and labelss_______
    
    #memberName---
    
    self.lbl_name=Label(self.bottomFrame,text="Name:",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_name.place(x=40,y=40)
    self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_name.insert(0,'Enter Member Name')
    self.ent_name.place(x=150,y=45)
    
    #PHone no-----
    
    self.lbl_phone=Label(self.bottomFrame,text="Phone:",font='arial 15 bold',fg='white',bg='#020875')
    self.lbl_phone.place(x=40,y=80)
    self.ent_phone=Entry(self.bottomFrame,width=30,bd=4)
    self.ent_phone.insert(0,'Enter Phone No:')
    self.ent_phone.place(x=150,y=85)
    
    
    
    ##Buttonn---------
    btn=Button(self.bottomFrame,text='Add Member',command=self.addMember)
    btn.place(x=270,y=120)
    
  def addMember(self):
    name=self.ent_name.get()
    phone=self.ent_phone.get()
    
   
    
    if (name and phone !=""):
      try:
        query = "INSERT INTO 'members'(member_name,member_phone) VALUES(?,?) "
        cur.execute (query,(name,phone))
        con.commit()
        messagebox.showinfo("success","successfully added to data base!",icon='info')
        self.destroy()
      
      except:
        messagebox.showerror("Error","can't add to data base",icon='warning')
    else :
        messagebox.showerror("Error","Fields cant be empty",icon='warning')