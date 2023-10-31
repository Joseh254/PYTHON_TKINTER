from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("message box program")


def message():
    c=messagebox.showerror("this is  my message", "you must be 18+")
    label = Label(root,text=c)

def mess():
    h=messagebox.askyesno("this is  my message", "are you  18+?")
    label = Label(root,text=h)

global a
a=10
if 13>a:
      Button(root, text="click", command=message).pack()
else:
        Button(root, text="click", command=mess).pack()

root.mainloop()
