
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
root = Tk()


def submit_data():


    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = label_combo.get()
    age = spinbox_age.get()
    nationality = combobox_nationality.get()

    year = combobox_year_of_study.get()
    semester = combobox_semester.get()
    registration_stat_us = registration_status.get()
    terms = conditions.get()
    accepted = conditions.get()
    if accepted == "accepted":
        if first_name:
            if last_name:

                conn = sqlite3.connect("form_database.db")
                table = """CREATE TABLE IF NOT EXISTS student_details
                    (firstname TEXT,
                    lastname TEXT,
                    Age INT,
                    Title TEXT,
                    Nationality TEXT,
                    year INT,
                    Semester INT,
                    Registration TEXT,
                    Terms TEXT)"""
                conn.execute(table)
                insert_query = """INSERT INTO student_details
                    (firstname,lastname,Age,Title,Nationality,Year, Semester,Registration,Terms)
                    VALUES(?,?,?,?,?,?,?,?,?)"""
                insert_tuple = (
                    first_name, last_name,  age, title, nationality, year, semester, registration_stat_us, terms)

                c = conn.cursor()
                c.execute(insert_query, insert_tuple)
                conn.commit()
                conn.close()
                first_name_entry.delete(0, END)
                last_name_entry.delete(0, END)
                label_combo.delete(0, END)
                spinbox_age.delete(0, END)
                combobox_nationality.delete(0, END)
                combobox_year_of_study.delete(0, END)
                combobox_semester.delete(0, END)


            else: messagebox.showwarning(title="Error", message="Last name field is empty")
        else: messagebox.showwarning(title="Error", message="First name field is empty")
    else: messagebox.showwarning(title="Error!", message="accept terms and conditions")
root.title("data entry form")
root.configure(bg="grey")
root.minsize(500, 500)
root.maxsize(500, 600)
frame = Frame(root)
frame.pack()


# saving user info
user_info_frame = LabelFrame(frame, text="user information", padx=20, pady=20)
user_info_frame.grid(row=0, column=0)

first_name_label = Label(user_info_frame, text="First Name")
last_name_label = Label(user_info_frame, text="last Name")
first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)

label_title = Label(user_info_frame, text="title")
label_combo = ttk.Combobox(user_info_frame, values=["", "Mr", "Mrs", "Dr"])

label_age = Label(user_info_frame, text="Age")

spinbox_age = Spinbox(user_info_frame, from_=18, to=100)

label_nationality = Label(user_info_frame, text="Nationality")
combobox_nationality = ttk.Combobox(user_info_frame, values=["Kenya", "DRC", "Uganda", "Tanzania", "Sudan", "Somalia"])


first_name_label.grid(row=0, column=0)
last_name_label.grid(row=0,  column=1)
last_name_entry.grid(row=1, column=1)
first_name_entry.grid(row=1, column=0)
label_combo.grid(row=1, column=2)
label_title.grid(row=0, column=2)
label_age.grid(row=2, column=0)
spinbox_age.grid(row=3, column=0)
label_nationality.grid(row=4, column=0)
combobox_nationality.grid(row=5, column=0)

# padding all widgets in user_info_frame
for Widget in user_info_frame.winfo_children():
    Widget.grid_configure(padx=10, pady=5)

# creating another frame for course registration
course_registration_frame = LabelFrame(frame, text="institution details", padx=20, pady=20)
course_registration_frame.grid(row=1, column=0, sticky="news", pady=20, padx=20)


label_registration_status = Label(course_registration_frame, text="Registration status")
registration_status = StringVar(value="Not Registered")
check_box_registered = Checkbutton(course_registration_frame, text="Registered", variable=registration_status,
                                   onvalue="Registered", offvalue="Not Registered")

label_number_of_semesters = Label(course_registration_frame, text="Semester")
combobox_semester = ttk.Combobox(course_registration_frame, values=["Not Enrolled", "1", "2"])
label_year_of_study = Label(course_registration_frame, text="Year Of Study")
combobox_year_of_study = ttk.Combobox(course_registration_frame, values=["1", "2", "3", "4"])


label_registration_status.grid(row=0, column=0)
check_box_registered.grid(row=1, column=0)

label_number_of_semesters.grid(row=0, column=2)
combobox_semester.grid(row=1, column=2)

label_year_of_study.grid(row=0, column=1)
combobox_year_of_study.grid(row=1, column=1)

for Widget in course_registration_frame.winfo_children():
    Widget.grid_configure(padx=10, pady=5)


# terms and condition frame
frame_terms = Frame(frame)
frame_terms.grid(row=2, column=0, sticky="news", pady=20, padx=20)

label_terms = Label(frame_terms, text="Terms & conditions")

conditions = StringVar(value="Terms not accepted")
checkbox_terms = Checkbutton(frame_terms, text="I accept terms & conditions", variable=conditions, onvalue="accepted", offvalue="Terms not accepted")
label_terms.grid(row=0, column=0)
checkbox_terms.grid(row=1, column=0)

for Widget in frame_terms.winfo_children():
    Widget.grid_configure(padx=10, pady=5)

# button frame
button_frame = Frame(frame)
button_save = Button(button_frame, text="Submit", command=submit_data)

button_frame.grid(row=3, column=0, sticky="news", padx=20, pady=20)
button_save.grid(row=0, column=0)
root.mainloop()
