import tkinter
from tkinter import *
from tkinter import messagebox
import random


def random_no():
    a = random.randint(1, 49);
    b = random.randint(1, 49);
    c = random.randint(1, 49);
    d = random.randint(1, 49);
    e = random.randint(1, 49);
    f = random.randint(1, 49);
    lottoNum1.set(a)
    lottoNum2.set(b)
    lottoNum3.set(c)
    lottoNum4.set(d)
    lottoNum5.set(e)
    lottoNum6.set(f)
    return


lotto = Tk()
lotto.title("Ithuba Lottery: Lotto Numbers")
lotto.geometry('400x300')
frame = Frame(lotto)
frame.pack()

lottoNum1 = StringVar()
lottoNum2 = StringVar()
lottoNum3 = StringVar()
lottoNum4 = StringVar()
lottoNum5 = StringVar()
lottoNum6 = StringVar()
