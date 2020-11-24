import random
from tkinter import *


window = Tk()
window.geometry = ("1200x900")
window.title("Ithuba Lottery: Lottery Numbers")

system_label = Label(window, text = "Ithuba Lottery: Lotto Numbers", font = ('Arial Black',30))
system_label.place(x=550,y=5)

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

label1 = LabelFrame(window, text = "Text", bd = 20, insertwidth = 1, font =("Arial",20), justify = CENTER)
#playButton = Button(window, text = "Press to Play", command = pick)

window.mainloop()
