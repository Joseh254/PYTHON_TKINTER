from tkinter import *

root = Tk()
# creating a title
root.title("CALCULATOR")
# creating an entry(textbox)

myentry = Entry(root, borderwidth=5)
myentry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
myentry.insert(0, 0)

# function to be called
# passing a paremeter
def button_click(number):

    current = myentry.get()
    #deleting the previuous input
    myentry.delete(0, END)
    #inserting a new input
    myentry.insert(0, str(current) + str(number))


def button_del():
    myentry.delete(0, END)

def button_add():
   first_number=myentry.get()
   global f_num
   global math
   math='addition'
   f_num = int(first_number)
   myentry.delete(0,END)

def button_subtract():
   first_number=myentry.get()
   global f_num
   global math
   math = 'subtraction'
   f_num=int(first_number)
   myentry.delete(0,END)

def button_multiply():
   first_number=myentry.get()
   global f_num
   global math
   math='multiplication'
   f_num=int(first_number)
   myentry.delete(0,END)

def button_divide():
   first_number=myentry.get()
   global f_num
   global math
   math="division"
   f_num=int(first_number)
   myentry.delete(0,END)

def button_equal():
    second_number=myentry.get()
    myentry.delete(0,END)
    if math=="addition":
      myentry.insert(0,int(f_num) + int(second_number))

    if math=="subtraction":
      myentry.insert(0,int(f_num) - int(second_number))

    if math=="multiplication":
      myentry.insert(0,int(f_num) * int(second_number))

    if math=="division":
      myentry.insert(0,int(f_num) / int(second_number))




# create buttons
button1 = Button(root, text="1", pady=20, padx=40, command=lambda: button_click(1),bg="grey",fg="white")
button2 = Button(root, text="2", pady=20, padx=40, command=lambda: button_click(2),bg="grey",fg="white")
button3 = Button(root, text="3", pady=20, padx=40, command=lambda: button_click(3),bg="grey",fg="white")
button4 = Button(root, text="4", pady=20, padx=40, command=lambda: button_click(4),bg="grey",fg="white")
button5 = Button(root, text="5", pady=20, padx=40, command=lambda: button_click(5),bg="grey",fg="white")
button6 = Button(root, text="6", pady=20, padx=40, command=lambda: button_click(6),bg="grey",fg="white")
button7 = Button(root, text="7", pady=20, padx=40, command=lambda: button_click(7),bg="grey",fg="white")
button8 = Button(root, text="8", pady=20, padx=40, command=lambda: button_click(8),bg="grey",fg="white")
button9 = Button(root, text="9", pady=20, padx=40, command=lambda: button_click(9),bg="grey",fg="white")
button0 = Button(root, text="0", pady=20, padx=40, command=lambda: button_click(0),bg="grey",fg="white")
button_subtract = Button(root, text="-", pady=20, padx=40, command=button_subtract,bg="green",fg="white")
button_division = Button(root, text="*", pady=20, padx=40, command=button_multiply,bg="green",fg="white")
button_multiplication = Button(root, text="/", pady=20, padx=40, command= button_divide,bg="green",fg="white")
buttonadd = Button(root, text="+", pady=20, padx=40, command=button_add,bg="green",fg="white")
buttonexit = Button(root, text="Exit", pady=20, padx=40, command=root.quit,bg="red",fg="white")
buttonequal = Button(root, text="=", pady=20, padx=40, command=button_equal,bg="blue",fg="white")
buttonedel = Button(root, text="del", pady=20, padx=40, command=button_del,fg="white",bg="black",width=2,height=1)
# put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=4, column=1)
buttonequal.grid(row=5, column=2)

button_subtract.grid(row=4, column=2)
button_multiplication.grid(row=5, column=0)
button_division.grid(row=5, column=1)
buttonedel.grid(row=6, column=0)
buttonexit.grid(row=6,column=2)

root.mainloop()
