from tkinter import *
import tkinter.messagebox
import SA.Sql#User defined module
import time
import os
def real():
       mn=Tk()
       mn.geometry('510x130+120+120')
       mn.title("Welcome to MySql")
       a=Label(mn,text="Enter Name:",bg="red",fg="white",font="Times 15")
       b=Label(mn,text="Enter Rollno.:",bg="blue",fg="white",font="Times 15")
       c=Label(mn,text="   Enter %:",bg="green",fg="white",font="Times 15")
       d=Button(mn,text="Submit",command=pn,bg="black",fg="white",font="Times 15")
       e=Button(mn,text="Report Analysis",command=nw,bg="orange",fg="white",font="Times 15")
       f=Button(mn,text="Delete",command=dlt,bg="black",fg="red",font="Times 15")
       a.grid(row = 0,column = 0,sticky=E)
       b.grid(row = 1,column = 0,sticky=E)
       c.grid(row = 2,column = 0,sticky=E)
       d.grid(column=1)
       e.grid(row=3,column=2)
       f.grid(row=3,column=0)
       global name
       global roll
       global percent
       global a1
       global b1
       global c1
       name=StringVar()
       roll=StringVar()
       percent=StringVar()
       a1 = Entry(mn,textvariable=name,font="Times 15")
       b1 = Entry(mn,textvariable=roll,font="Times 15")
       c1 = Entry(mn,textvariable=percent,font="Times 15")
       a1.grid(row = 0,column = 1)
       b1.grid(row = 1,column = 1)
       c1.grid(row = 2,column = 1)
       mn.mainloop()

def pn(): 
       SA.Sql.add(str(name.get()),str(roll.get()),str(percent.get()))
       a1.delete(0,END)
       b1.delete(0,END)
       c1.delete(0,END)
       tkinter.messagebox.showinfo('Thanks for submitting','Successfully uploaded')        
def nw():
       result=SA.Sql.pp()

       jc=SA.Sql.top()

       top=Toplevel()
       top.geometry('510x220+120+120')
       top.title("Report Analysis")
       ps=Label(top,text="Total number of students:"+str(result[0]),fg="black",font="Times 15")
       pd=Label(top,text="Percentage of students passed:"+str(round((result[1]),1))+"%",fg="black",font="Times 15")
       av=Label(top,text="Average Score:"+str(result[2])+"%",fg="black",font="Times 15")
       tp=Label(top,text="Topper details:",fg="black",font="Times 15")
       nm=Label(top,text="Name",fg="black",font="Times 15")
       mrk=Label(top,text="Marks",fg="black",font="Times 15")
       tp1=Label(top,text=str(jc[0][0]),fg="black",font="Times 15")
       tp11=Label(top,text=str(jc[0][2]),fg="black",font="Times 15")
       tp2=Label(top,text=str(jc[1][0]),fg="black",font="Times 15")
       tp22=Label(top,text=str(jc[1][2]),fg="black",font="Times 15")
       tp3=Label(top,text=str(jc[2][0]),fg="black",font="Times 15")
       tp33=Label(top,text=str(jc[2][2]),fg="black",font="Times 15")
       ps.grid(row = 0,column = 0,sticky=W)
       pd.grid(row = 1,column = 0,sticky=W)
       av.grid(row = 2,column = 0,sticky=W)
       tp.grid(row = 3,column = 0,sticky=E)
       nm.grid(row = 4,column = 0,sticky=W)
       mrk.grid(row = 4,column = 0,sticky=E)
       tp1.grid(row = 5,column = 0,sticky=W)
       tp11.grid(row = 5,column = 0,sticky=E)
       tp2.grid(row = 6,column = 0,sticky=W)
       tp22.grid(row = 6,column = 0,sticky=E)
       tp3.grid(row = 7,column = 0,sticky=W)
       tp33.grid(row = 7,column = 0,sticky=E)
def login():
       global mt
       mt=Tk()
       mt.geometry('510x130+120+120')
       mt.title("Please login")
       global usr
       global pwd
       usr=StringVar()
       pwd=StringVar()
       a=Label(mt,text="Enter UserName:",font="Times 15")
       b=Label(mt,text="Enter Password:",font="Times 15")
       global a1
       global b1
       global z
       z=0
       a1 = Entry(mt,textvariable=usr,font="Times 15")
       b1 = Entry(mt,show='*',textvariable=pwd,font="Times 15")
       
       c=Button(mt,text="Login",command=click,bg="black",fg="white",font="Times 15")
           
       a.grid(row = 0,column = 0,sticky=W)
       b.grid(row = 1,column = 0,sticky=W)
       c.grid(column=1)
       a1.grid(row = 0,column = 1)
       b1.grid(row = 1,column = 1)
       mt.mainloop()


def click():
		
        if usr.get()=="ussername" and pwd.get()=="password":
             localtime = time.asctime( time.localtime(time.time()) )
             f=open(r"file location ","a+")
             f.write("User : "+str(usr.get())+" logged in @ "+localtime+'\n')
             f.close()
             mt.destroy()

             real()
        else:
            
            tkinter.messagebox.showinfo('Wrong Credentials','Wrong Username/Password!!')        
            a1.delete(0,END)
            b1.delete(0,END)
def remo():
       SA.Sql.dlttt(str(text.get()))
       tkinter.messagebox.showinfo('Alert Mesage','Deleted Record!!')        
       Dt.delete(0,END)
       dl.destroy()
       
def dlt():
       global dl
       global Dt
       global text
       dl=Tk() 
       text=StringVar()
       dl.geometry('510x130+120+120')
       dl.title("Delete record")
       Dt = Entry(dl,textvariable=text,font="Times 15")
       a=Label(dl,text="Enter Name:",fg="black",font="Times 15")
       a.grid(row = 0,column = 0,sticky=E)
       
       SA.Sql.dltt()
       
       
       d=Button(dl,text="Delete",command=remo,bg="black",fg="white",font="Times 15")
       d.grid(column=1)
       Dt.grid(row = 0,column = 1)
       dl.mainloop()

       

       

login()

