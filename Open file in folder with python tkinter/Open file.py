from tkinter import*
from tkinter import filedialog
root = Tk()
root.title('Open file')
root.configure(bg='#6A5A99')
root.geometry('400x200')

def open_file():
    types = [('All files', '*.*'),('Text files','*.txt')]
    path = filedialog.askopenfilename(initialdir=".", title='Open file', filetypes=types)
    file = open(path, "r")
    text = Text(root, font=('aerial', 10, 'bold'), relief=SUNKEN, bd=5, bg='#DBF9DB', width=40, height=20,fg='black')
    text.pack(pady=10)
    text.insert(1.0,file.read)
    file.close()
button = Button(root, text='Open file', command=open_file, font=('aerial', 10, 'bold'),
                relief=SUNKEN, bd=5, bg='#848B79', width=20, height=1, activebackground='yellow')
button.pack()
root.mainloop()