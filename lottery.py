import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
from tkinter import ttk


mywindow = Tk()
mywindow.geometry = ("600x600")
mywindow.title("Ithuba Lottery: Lottery Numbers")

#random_no = random.randint(range(1, 49),6)
randomz = list(range(1,49))
lottoNum = []

for i in range(6):
    shuffle(randomz)
    n = randomz.pop()
    lottoNum.append(n)

lottoNum.sort()





mywindow.mainloop()
