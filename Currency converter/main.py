from tkinter import*
window = Tk()
window.geometry('400x400')
window.title('Currency converter program')
window.resizable ('false', 'false')
window.configure(bg= 'gold')
from tkinter import messagebox
def convert():
    if entry_enter.get() =='':
        messagebox.showerror('Error','Amount field is empty')
    if entry_enter.get()=='0':
        messagebox.showerror('Error','Amount cannot be zero')
    else:

        result = int(entry_enter.get())/160
        string = str(result) + ' USD'
        label_result.config(text = string)
        entry_enter.delete(0, END)
label_linee = Label(window,text ='Convert to Usd', bg = 'gold',height = 1, font = ('times new roman', 16, 'bold'))
label_linee.grid(row=0, column=0)
label_enter = Label(window, text = 'Enter amount in Ksh', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'black', width = 20, height = 1,
                    relief = GROOVE)
label_enter.grid(row=1, column=0)
entry_enter = Entry(window, bd = 5, font = ('times new roman', 10, 'bold'), width = 20, relief =
                    SUNKEN)
entry_enter.grid(row = 1, column =1, padx=20)

button_convert = Button(window, text = 'Convert', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'grey20', width = 15, height = 2,
                        command = convert)

button_convert.grid(row=2, column=1, padx=10, pady=20)

label_result = Label(window, text = 'Result', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'black', width = 15,
                     relief = GROOVE)
label_result.grid(row=3, column=1)
label_line = Label(window,text ='Convert to Ksh', bg = 'gold',height = 1, font = ('times new roman', 16, 'bold'))
label_line.grid(row=4, column=0)

def convertt():
    if entry_enter_amt.get()=="" :
        messagebox.showerror('Error','Amount field is empty')
    if entry_enter_amt.get()=='0':
        messagebox.showerror('Error','Amount cannot be zero')
    else:
        amt = int(entry_enter_amt.get())*160
        stringg = str(amt)+' Ksh'
        label_resultt.config(text = stringg)
        entry_enter_amt.delete(0, END)


label_enter_ = Label(window, text = 'Enter amount in Usd', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'black', width = 20, height = 1,
                    relief = GROOVE)
label_enter_.grid(row=5, column=0)
entry_enter_amt = Entry(window, bd = 5, font = ('times new roman', 10, 'bold'), width = 20, relief =
                    SUNKEN)
entry_enter_amt.grid(row = 5, column =1, padx=20)

button_convertt = Button(window, text = 'Convert', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'grey20', width = 15, height = 2,
                        command = convertt)

button_convertt.grid(row=6, column=1, padx=10, pady=20)

label_resultt = Label(window, text = 'Result', bd = 5, font = ('times new roman', 10, 'bold'), fg = 'black', width = 15,
                     relief = GROOVE)
label_resultt.grid(row=7, column=1)


window.mainloop()