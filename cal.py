from tkinter import *
import time
clock=Tk()
clock.title(' enri media ')
clock.geometry("500x300")
clock.config(bg="purple")
labh=Label(clock,text=time.strftime("%a,%d %h %Y"),font=("Time New Roman",40,"bold"),bg="purple",fg='yellow')
labh.place(x=40,y=40)
labs=Label(clock,text=time.strftime("%D"),font=("Time New Roman",40,"bold"),bg='purple',fg='yellow')
labs.place(x=40,y=120)
labh=Label(clock,text=time.strftime("%r"),font=("Time New Roman",40,"bold"),bg='purple',fg='yellow')
labh.place(x=40,y=200)
clock.mainloop()
