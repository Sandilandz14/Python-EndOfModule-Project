from datetime import *
from tkinter import *
from tkinter import messagebox
import random


window = Tk()
window.geometry = ("300x300")
window.title("Ithuba Lottery: Age Restriction")
window.resizable(False,False)
random_no = random.sample(range(1,49), 6)

lottery = []
name_ = Entry(window, width=15)
name_.place(x=60,y=50)
name_label = Label(window, text="Name:")
name_label.place(x=10, y=50)

age_num = Entry(window, text="Age:", width=15)
age_num.place(x=60,y=80)
age_label = Label(window, text="Age:")
age_label.place(x=10, y=80)

date_label = Label(window)
date_label.config(text="Date: "+datetime.now().strftime("%m/%d/%y"))

file = "sandile.txt"



def age_confirm():
    try:
        if int(age_num.get()) < 18:
            messagebox.showwarning("Error!", "You are underage!")
            window.destroy()

        elif int(age_num.get()) >= 18:

         yourName = name_.get()
         yourAge = age_num.get()
         currentDate = str(date_label.cget("text"))
         messagebox.display("Go through","Proceed to play lotto!!!!!!!")



    except:
        if age_num is str:
            messagebox.showinfo("Enter valid input")


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
            num_A = Entry(my_window,width=6)
            num_A.place(x=5,y=25)
            num_B = Entry(my_window,width=6)
            num_B.place(x=50,y=25)
            num_C = Entry(my_window,width=6)
            num_C.place(x=5,y=45)
            num_D = Entry(my_window,width=6)
            num_D.place(x=50,y=45)
            num_E = Entry(my_window,width=6)
            num_E.place(x=5,y=65)
            num_F = Entry(my_window,width=6)
            num_F.place(x=50,y=65)
            label_this = Label(my_window, text="Enter Lotto numbers:")
            label_this.place(x=5, y=5)
            outcome_label = Label(my_window)
            outcome_label.place(x=5,y=130)

        except ValueError as e:
            messagebox.showerror("Error", "Enter number"+e)
            # function to append the list and
            # decide how many numbers you got correct

        def lottoFunction():

            lottery.append(int(num_A.get()))
            lottery.append(int(num_B.get()))
            lottery.append(int(num_C.get()))
            lottery.append(int(num_D.get()))
            lottery.append(int(num_E.get()))
            lottery.append(int(num_F.get()))


            correct_numbers = set(lottery).intersection(random_no)

            if lottery == random_no:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"You got all correct\n" + "These are the outcomes: " + str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"YOU WON R10 000 000.00"+"\n"+currentDate)
            elif len(correct_numbers) == 0:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 0 correct\n" + "These are the outcomes: "+ str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won nothing..."+"\n"+currentDate)
            elif len(correct_numbers) == 1:
               outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 1 correct\n" + "These are the outcomes: "+ str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won nothing..."+"\n"+currentDate)
            elif len(correct_numbers) == 2:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 2 correct\n" + "These are the outcomes: " + str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won R20"+"\n"+"\n"+currentDate)
            elif len(correct_numbers) == 3:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 3 correct\n" + "These are the outcomes: "+ str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won R100.50"+"\n"+"\n"+currentDate)
            elif len(correct_numbers) == 4:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 4 correct\n" +"These are the outcomes: "+ str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won R2,384.00"+"\n"+currentDate)
            elif len(correct_numbers)== 5:
                outcome_label.config(text="Name: "+yourName+"\n"+"Age: "+yourAge+"\n"+"Sorry you got 5 correct\n" + "These are the outcomes: "+ str(sorted(random_no[0:5])) +"\n" +"Jackpot ball is: "+ str(random_no[5]) +"\n"+"You won R8,584.00"+"\n"+currentDate)
            f = open(file, "w+")
            f.close()
            f = open(file, "a")
            outcomes = outcome_label.cget("text")
            f.write(outcomes)
            f.close()

        lottoFunc_button = Button(my_window, text="Check Outcomes", command=lottoFunction)
        lottoFunc_button.place(x=5,y=90)


age_button = Button(window, command=age_confirm, text="Enter Lotto")
age_button.place(x=90,y=105)
date_label.place(x=10,y=20)
window.mainloop()
