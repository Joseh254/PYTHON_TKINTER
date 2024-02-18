from tkinter import*
from tkinter import filedialog,messagebox

root = Tk()
root.title('Save file')


def save_file():

    type = [('All files', '*.*'),('Text file', '*.txt')]
    path = filedialog.asksaveasfilename(initialdir='.', filetypes=type, title='Save file')
    file = text.get(1.0, END)
    file_save = open(path,'w')
    file_save.write(file)
    file_save.close()
    messagebox.showinfo('Success', 'File saved succesfuly')


Label = Label(root, text='Enter a text', font=('aerial', 14, 'bold'), relief=GROOVE)
Label.grid(row=0, column=1, padx=10)
text = Text(root, font=('aerial', 10, 'bold'), relief=SUNKEN, bd=5, bg='#DBF9DB', width=40, height=20,fg='black')
text.grid(row=1, column=1, padx=10)
button = Button(root, text='save', relief=RAISED, command=save_file, bg='#95B9C7', width='15')
button.grid(row=2, column=1, pady=14)
root.mainloop()