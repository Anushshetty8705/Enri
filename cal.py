from tkinter import *
import time
def data():
    ttime=time.strftime('%r')
    dateformate=time.strftime("%a,%d %h %Y")
    standard_date=time.strftime("%d/%m/%y")
    no_week=time.strftime("Week No : %W")
    labs.config(text=standard_date)
    labe.config(text=ttime)
    labh.config(text=dateformate)
    lab_week.config(text=no_week)
    labs.after(200,data)
clock=Tk()
clock.title(' enri media ')
clock.geometry("500x400")
clock.config(bg="purple")
labh=Label(clock,font=("Palatino",40),bg="purple",fg='yellow')
labh.place(x=40,y=40)
labs=Label(clock,font=("palatino",40),bg='purple',fg='yellow')
labs.place(x=40,y=120)
labe=Label(clock,font=("palatino",40),bg='purple',fg='yellow')
labe.place(x=40,y=200)
lab_week=Label(clock,font=("palatino",40),bg='purple',fg='yellow')
lab_week.place(x=40,y=280)
data()
clock.mainloop()
