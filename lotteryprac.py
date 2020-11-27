import tkinter
from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk


window = Tk()
window.geometry = ("300x300")
window.title("Ithuba Lottery: Age Restriction")

random_no = random.randint(range(1,49),6)
lottery = []
name_ = Entry(window)
name_lb = Label(window, text="Name:")

age_num = Entry(window, text="Age:")
age_label = Label(window, text="Age:", width=5)

file = "Lotto.txt"

def age_confirm():
    try:
        if int(age_num.get()) < 18:
            messagebox.showwarning()("Error!", "You are underage")
        if int(age_num.get()) >= 18:

         nameVar = name_.get()
        ageVar = age_num.get()

        window.destroy()
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
        my_window = Tk()
        my_window.geometry = ("400x400")
        my_window.title("Ithuba Lottery: Lottery Numbers")
        #
        # system_label = Label(my_window, text = "Ithuba Lottery: Lotto Numbers", font = ('Arial Black',30))
        # system_label.place(x=300,y=5)


        try:
            #Creates widgets to enter numbers
            # and labels
            num_A = Entry(my_window,width=10)
            num_B = Entry(my_window,width=10)
            num_C = Entry(my_window,width=10)
            num_D = Entry(my_window,width=10)
            num_E = Entry(my_window,width=10)
            num_F = Entry(my_window,width=10)
            lb = Label(my_window, text="Enter Lotto numbers:")
            result_lb = Label(my_window)
        except ValueError as e:
            messagebox.showerror("Error", "Enter number"+e)



        def lottoNumbers():
                a = random.randint(1, 49)
                b = random.randint(1, 49)
                c = random.randint(1, 49)
                d = random.randint(1, 49)
                e = random.randint(1, 49)
                f = random.randint(1, 49)
                lottoNum1.set(a)
                lottoNum2.set(b)
                lottoNum3.set(c)
                lottoNum4.set(d)
                lottoNum5.set(e)
                lottoNum6.set(f)
                return


        lottoNum1 = StringVar()
        lottoNum2 = StringVar()
        lottoNum3 = StringVar()
        lottoNum4 = StringVar()
        lottoNum5 = StringVar()
        lottoNum6 = StringVar()
        #
            # label1 = LabelFrame(window, text = "Text", bd = 20, insertwidth = 1, font =("Arial",20), justify = CENTER)
            # #playButton = Button(window, text = "Press to Play", command = pick)
window.mainloop()
