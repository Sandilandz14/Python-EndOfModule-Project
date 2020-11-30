import tkinter
from datetime import *
from tkinter import *
from tkinter import messagebox
import random
from random import randint
from tkinter import ttk
window = Tk()
window.geometry = ("300x300")
window.title("Ithuba Lottery: Age Restriction")


#random_no = random.randint(range(1,49),6)
lottery = []
name_ = Entry(window, width=7)
name_.place(x=60,y=50)
name_label = Label(window, text="Name:")
name_label.place(x=10, y=50)

age_num = Entry(window, text="Age:", width=7)
age_num.place(x=60,y=80)
age_label = Label(window, text="Age:")
age_label.place(x=10, y=80)

date_label = Label(window)
date_label.config(text="Date: "+datetime.now().strftime("%m/%d/%y"))

file = "Lotto.txt"



def age_confirm():
    try:
        if int(age_num.get()) < 18:
            messagebox.showwarning()("Error!", "You are underage")
        if int(age_num.get()) >= 18:

         nameVar = name_.get()
         ageVar = age_num.get()
         dateVar = str(date_label.cget("text"))
         messagebox.showinfo("Go through","Proceed to play lotto!!!!!!!")

         window.destroy()

    except:
        if age_num is str:
            print("Enter valid input")

age_button = Button(window, command=age_confirm, text="Enter Lotto")
age_button.place(x=90,y=105)
window.mainloop()
