from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import random
import os
import tempfile
import smtplib


def system_window():
    if entry_user_name.get() != 'jose' or entry_password.get() != '1234':
        messagebox.showerror('Error', 'user name or password is incorrect')
    if entry_user_name.get() == '' or entry_password.get() == '':
        messagebox.showerror('error', 'all fields are required')
    if entry_user_name.get() == 'jose' and entry_password.get() == '1234':

        top = Toplevel()
        top.geometry('1366x768')
        top.title('Mbugua Retail Management System')
        top.resizable(False, False)
        top.configure(bg = '#696969')
        global bill_number
        bill_number = random.randint(100, 1000)

        if not os.path.exists('bills'):
            os.mkdir('bills')


        def exit():
            yes = messagebox.askyesno('Confirm', 'Are you sure you want to exit?')
            if yes:
                top.quit()
                login_window.destroy()
            else:
                system_window()


        def email():
            def send_email():
                ob = smtplib.SMTP('smtp.gmail.com', 587)
                ob.starttls()
                ob.login(entry_sender_email.get(), entry_pass.get())
                message = text_area.get(1.0, END)
                receiver_adress = entry_recepient_email.get()
                ob.sendmail(entry_sender_email.get(), receiver_adress, message)
                ob.quit()
                messagebox.showinfo('Sucess', 'Mail sent')
                system_window()
            if bill_text_area.get(1.0, END) =='\n':
                messagebox.showerror('Error', 'Bill is Empty')
                system_window()
            else:
                email = Toplevel()
                email.title('Send Email')
                email.configure(bg = 'grey20')
                email.resizable(False, False)
                sender_frame = LabelFrame(email, text = 'SENDER', font = ('airial', '16', 'bold'), bd = 6, bg = 'grey20',
                                          fg = '#00fa9a')
                sender_frame.grid(row = 0, column = 0)
                label_sender = Label(sender_frame, text = 'Senders email', font = ('airial', '14', 'bold'), bg = 'grey20',
                                     fg = '#20b2aa')
                label_sender.grid(row = 0, column = 0)
                label_Pass = Label(sender_frame, text = "Password", font = ('airial', '14', 'bold'), bg = 'grey20',
                                   fg = '#20b2aa')
                label_Pass.grid(row = 1, column = 0)
                entry_sender_email = Entry(sender_frame, width = 30, font = ('airial', '16', 'bold'))
                entry_sender_email.grid(row = 0, column = 1, padx = 8, pady = 10)
                entry_sender_email.insert(0, 'josephkarimambugua@gmail.com')
                entry_pass = Entry(sender_frame, width = 30, show = '*', font = ('airial', '16', 'bold'))
                entry_pass.grid(row = 1, column = 1, padx = 8, pady = 10)
                entry_pass.insert(0, 'ussr tgtb fwbx ufzx')

                recepient_frame = LabelFrame(email, text = 'RECIPIENT', font = ('airial', '16', 'bold'), bg = 'grey20',
                                             fg = '#00fa9a')
                recepient_frame.grid(row = 1, column = 0, padx = 20, pady = 40)
                label_recIpient_email = Label(recepient_frame, text = 'Receivers Email', font = ('airial', '16', 'bold'),
                                              bg = 'grey20', fg = '#20b2aa')
                label_recIpient_email.grid(row = 0, column = 0)
                entry_recepient_email = Entry(recepient_frame, font = ('airial', '16', 'bold'), width = 30)
                entry_recepient_email.grid(row = 0, column = 1, padx = 8, pady = 10)
                label_message = Label(recepient_frame, text = 'Message', font = ('airial', '16', 'bold'), bg = 'grey20',
                                      fg = '#20b2aa')
                label_message.grid(row = 1, column = 0, padx = 15, pady = 20)

                text_area = Text(recepient_frame, height = 14, width = 75, bg = '#f0f8ff', bd = 2, relief = SUNKEN)
                text_area.grid(row = 2, column = 0, columnspan = 2)
                text_area.delete(1.0, END)
                text_area.insert(END, bill_text_area.get(1.0, END))

                send_button = Button(email, text = "SEND", font = ('airial', '16', 'bold'), bg = 'khaki', fg = 'black',
                                     width = 20, command = send_email)
                send_button.grid(row = 2, column = 0)

                email.mainloop()

        def clear():
            entry_name.delete(0, END)
            phone_entry.delete(0, END)
            entry_hp_250g6.delete(0, END)
            entry_hp_1030g2.delete(0, END)
            entry_lenovo_x1carbon.delete(0, END)
            entry_dell_t460s.delete(0, END)
            entry_macbook_a1278.delete(0, END)
            entry_asus.delete(0, END)

            entry_hp_430g3.delete(0, END)
            entry_macbook_air.delete(0, END)
            entry_dell_latitude.delete(0, END)
            entry_lenovo_thinkpad.delete(0, END)
            entry_asuss.delete(0, END)
            entry_hp_9470.delete(0, END)

            entry_hp_820g2.delete(0, END)
            entry_lenovo_yoga_11e.delete(0, END)
            entry_dell_t470.delete(0, END)
            entry_lenovo_820_revolve.delete(0, END)
            entry_aasus.delete(0, END)
            entry_hp_chromebook.delete(0, END)

            bill_text_area.delete(1.0, END)
            entry_laptop_batteries_price.delete(0, END)
            entry_laptop_keyboards_price.delete(0, END)
            entry_laptop_motherboards_price.delete(0, END)
            entry_laptop_batteries_tax.delete(0, END)
            entry_laptop_keyboards_tax.delete(0, END)
            entry_laptop_motherboards_tax.delete(0, END)

            entry_hp_250g6.insert(0, '0')
            entry_hp_1030g2.insert(0, '0')
            entry_lenovo_x1carbon.insert(0, '0')
            entry_dell_t460s.insert(0, '0')
            entry_macbook_a1278.insert(0, '0')
            entry_asus.insert(0, '0')

            entry_hp_430g3.insert(0, '0')
            entry_macbook_air.insert(0, '0')
            entry_dell_latitude.insert(0, '0')
            entry_lenovo_thinkpad.insert(0, '0')
            entry_asuss.insert(0, '0')
            entry_hp_9470.insert(0, '0')

            entry_hp_820g2.insert(0, '0')
            entry_lenovo_yoga_11e.insert(0, '0')
            entry_dell_t470.insert(0, '0')
            entry_lenovo_820_revolve.insert(0, '0')
            entry_aasus.insert(0, '0')
            entry_hp_chromebook.insert(0, '0')

            entry_laptop_batteries_price.insert(0, '0')
            entry_laptop_keyboards_price.insert(0, '0')
            entry_laptop_motherboards_price.insert(0, '0')
            entry_laptop_batteries_tax.insert(0, '0')
            entry_laptop_keyboards_tax.insert(0, '0')
            entry_laptop_motherboards_tax.insert(0, '0')

        def print():
            if bill_text_area.get(1.0, END) == '\n':
                messagebox.showerror('Error', 'Bill is empty')
                system_window()
            else:
                file = tempfile.mktemp('.txt')
                open(file, 'w').write(bill_text_area.get(1.0, END))
                os.startfile(file, 'print')

        def search():
            for i in os.listdir('bills/'):
                c = entry_bill_number.get()
                if i.split('.')[0] == c:
                    j = open(f'bills/{i}', 'r')
                    bill_text_area.delete(1.0, END)
                    for data in j:
                        bill_text_area.insert(END, data)
                    j.close()
                    break
                else:
                    messagebox.showerror('Error', 'The bill number does not exist')
                    system_window()

        def save_bill():
            bill_content = bill_text_area.get(1.0, END)
            bill_number = random.randint(100, 1000)
            file = open(f'bills/ {bill_number}.txt', 'w')
            file.write(bill_content)
            file.close()

        def bill():
            bill_text_area.delete(1.0, END)
            if entry_name.get() == '' or phone_entry.get() == '':
                messagebox.showerror('Error', 'Customer details are required')
                system_window()

            elif entry_laptop_motherboards_price.get() == '' and entry_laptop_batteries_price.get() == '' and entry_laptop_keyboards_price.get() == '':
                messagebox.showerror('Error', 'No Products selected')
                system_window()

            elif entry_laptop_motherboards_price.get() == '0Ksh' and entry_laptop_batteries_price.get() == '0Ksh' and entry_laptop_keyboards_price.get() == '0Ksh':
                messagebox.showerror('Error', 'No Products purchased')
                system_window()
            else:

                bill_text_area.insert(END, '**********You were served by joseph**********\n')
                bill_text_area.insert(END, 'Bill Number: ' + str(bill_number))
                bill_text_area.insert(END, '\nCustomer Name: ' + str(entry_name.get()))
                bill_text_area.insert(END, '\nCustomer phone number: ' + str(phone_entry.get()))
                bill_text_area.insert(END, '\n=============================================')
                bill_text_area.insert(END, '\nPRODUCTS\t\tQUANTITY\t\tPRICE')
                bill_text_area.insert(END, '\n=============================================')
                if entry_hp_250g6.get() != '0':
                    bill_text_area.insert(END,
                                          '\nHp 250 g6 battery\t\t ' + str(entry_hp_250g6.get()) + '           ' + str(
                                              hp250g6) + 'Ksh')
                if entry_hp_1030g2.get() != '0':
                    bill_text_area.insert(END,
                                          '\nhp 1030 g2 battary\t\t' + str(entry_hp_1030g2.get()) + '           ' + str(
                                              hp1030g2) + 'Ksh')
                if entry_lenovo_x1carbon.get() != '0':
                    bill_text_area.insert(END, '\nx1carbon battary\t\t  ' + str(
                        entry_lenovo_x1carbon.get()) + '           ' + str(lenovo_x1carbon) + 'Ksh')
                if entry_dell_t460s.get() != '0':
                    bill_text_area.insert(END, '\nDell T460s battary\t\t' + str(
                        entry_dell_t460s.get()) + '           ' + str(dell_t460s) + 'Ksh')
                if entry_macbook_a1278.get() != '0':
                    bill_text_area.insert(END, '\nhp 1030 g2 battary\t\t' + str(
                        entry_macbook_a1278.get()) + '           ' + str(macbook_a1278) + 'Ksh')
                if entry_asus.get() != '0':
                    bill_text_area.insert(END, '\nhp 1030 g2 battary\t\t' + str(entry_asus.get()) + '           ' + str(
                        asus) + 'Ksh')

                if entry_hp_430g3.get() != '0':
                    bill_text_area.insert(END,
                                          '\nHp 430 g3 keyboard\t\t' + str(entry_hp_430g3.get()) + '           ' + str(
                                              hp430g3) + 'Ksh')
                if entry_macbook_air.get() != '0':
                    bill_text_area.insert(END, '\nmcbookair keyboard\t\t' + str(
                        entry_macbook_air.get()) + '           ' + str(macbook_air) + 'Ksh')
                if entry_dell_latitude.get() != '0':
                    bill_text_area.insert(END, '\nDell ltd  keyboard\t\t' + str(
                        entry_dell_latitude.get()) + '           ' + str(dell_latitude) + 'Ksh')
                if entry_lenovo_thinkpad.get() != '0':
                    bill_text_area.insert(END, '\nlv thikpad kyboard\t\t' + str(
                        entry_lenovo_thinkpad.get()) + '           ' + str(lenovo_thinkpad) + 'Ksh')
                if entry_asuss.get() != '0':
                    bill_text_area.insert(END,
                                          '\nAsus              \t\t' + str(entry_asuss.get()) + '           ' + str(
                                              asuss) + 'Ksh')
                if entry_hp_9470.get() != '0':
                    bill_text_area.insert(END,
                                          '\nhp 9470M kyboard  \t\t' + str(entry_hp_9470.get()) + '           ' + str(
                                              hp_9470) + 'Ksh')

                if entry_hp_820g2.get() != '0':
                    bill_text_area.insert(END,
                                          '\nhp 820g2 mtbrd    \t\t' + str(entry_hp_820g2.get()) + '           ' + str(
                                              hp820g2) + 'Ksh')
                if entry_lenovo_yoga_11e.get() != '0':
                    bill_text_area.insert(END, '\nyoga 11e mtbrd    \t\t' + str(
                        entry_lenovo_yoga_11e.get()) + '           ' + str(yoga11e) + 'Ksh')
                if entry_dell_t470.get() != '0':
                    bill_text_area.insert(END,
                                          '\ndell t470 mtbrd   \t\t' + str(entry_dell_t470.get()) + '           ' + str(
                                              dell_t470) + 'Ksh')
                if entry_lenovo_820_revolve.get() != '0':
                    bill_text_area.insert(END, '\n820 revolve mtbrd \t\t' + str(
                        entry_lenovo_820_revolve.get()) + '           ' + str(lenovo_820_revolve) + 'Ksh')
                if entry_aasus.get() != '0':
                    bill_text_area.insert(END,
                                          '\nAsus mothebrd     \t\t' + str(entry_aasus.get()) + '           ' + str(
                                              aasus) + 'Ksh')
                if entry_hp_chromebook.get() != '0':
                    bill_text_area.insert(END, '\nhpchromebok mtbrd \t\t' + str(
                        entry_hp_chromebook.get()) + '           ' + str(hp_chroomebook) + 'Ksh')
                bill_text_area.insert(END, '\n=============================================')
                if entry_laptop_keyboards_tax.get() > '1.0':
                    bill_text_area.insert(END, '\nTotal Keyboard tax ' + str(entry_laptop_keyboards_tax.get()))
                if entry_laptop_batteries_tax.get() > '1.0':
                    bill_text_area.insert(END, '\nTotal Laptop battery tax ' + str(entry_laptop_batteries_tax.get()))
                if entry_laptop_motherboards_tax.get() > '1.0':
                    bill_text_area.insert(END, '\nTotal Motherboard tax ' + str(entry_laptop_motherboards_tax.get()))
                bill_text_area.insert(END, '\n=============================================')
                bill_text_area.insert(END, '\nTotal Amount: ' + str(total_amount) + 'Ksh')
                bill_text_area.insert(END, '\n=============================================')
                bill_text_area.insert(END, '\n         Thank you for shopping with us')
                save_bill()

        def total():
            global hp250g6
            global hp1030g2
            global lenovo_x1carbon
            global dell_t460s
            global macbook_a1278
            global asus

            global hp430g3
            global macbook_air
            global dell_latitude
            global lenovo_thinkpad
            global asuss
            global hp_9470

            global hp820g2
            global yoga11e
            global dell_t470
            global lenovo_820_revolve
            global aasus
            global hp_chroomebook
            global total_amount

            hp250g6 = int(entry_hp_250g6.get())*2000
            hp1030g2 = int(entry_hp_1030g2.get())*2000
            lenovo_x1carbon = int(entry_lenovo_x1carbon.get())*2000
            dell_t460s = int(entry_dell_t460s.get())*2000
            macbook_a1278 = int(entry_macbook_a1278.get())*2000
            asus = int(entry_asus.get())*2000
            batteries_total = hp250g6 + hp1030g2 + lenovo_x1carbon + dell_t460s + macbook_a1278 + asus
            entry_laptop_batteries_price.delete(0, END)
            entry_laptop_batteries_price.insert(0, str(batteries_total) + 'Ksh')
            batteries_tax = batteries_total*0.1
            entry_laptop_batteries_tax.delete(0, END)
            entry_laptop_batteries_tax.insert(0, str(batteries_tax) + 'Ksh')

            hp430g3 = int(entry_hp_430g3.get())*1000
            macbook_air = int(entry_macbook_air.get())*1000
            dell_latitude = int(entry_dell_latitude.get())*1000
            lenovo_thinkpad = int(entry_lenovo_thinkpad.get())*1000
            asuss = int(entry_asuss.get())*1000
            hp_9470 = int(entry_hp_9470.get())*1000
            keyboard_total = hp430g3 + macbook_air + dell_latitude + lenovo_thinkpad + asuss + hp_9470
            entry_laptop_keyboards_price.delete(0, END)
            entry_laptop_keyboards_price.insert(0, str(keyboard_total) + 'Ksh')
            keyboard_tax = keyboard_total*0.01
            entry_laptop_keyboards_tax.delete(0, END)
            entry_laptop_keyboards_tax.insert(0, str(keyboard_tax) + 'Ksh')

            hp820g2 = int(entry_hp_820g2.get())*3500
            yoga11e = int(entry_lenovo_yoga_11e.get())*3500
            dell_t470 = int(entry_dell_t470.get())*3500
            lenovo_820_revolve = int(entry_lenovo_820_revolve.get())*3500
            aasus = int(entry_aasus.get())*3500
            hp_chroomebook = int(entry_hp_chromebook.get())*3500
            motherboad_total = hp820g2 + yoga11e + dell_t470 + lenovo_820_revolve + asus + hp_chroomebook
            entry_laptop_motherboards_price.delete(0, END)
            entry_laptop_motherboards_price.insert(0, str(motherboad_total) + 'Ksh')
            motherboard_tax = motherboad_total*0.1
            entry_laptop_motherboards_tax.delete(0, END)
            entry_laptop_motherboards_tax.insert(0, str(motherboard_tax) + 'Ksh')

            total_amount = motherboad_total + motherboard_tax + keyboard_tax + keyboard_total + batteries_total + batteries_tax

        system_frame = Frame(top)
        system_frame.pack()

        heading_label = Label(system_frame, text = 'Secure Retail Management System',
                              font = ('times new roman', 30, 'bold'), bg = 'grey20', fg = '#6495ed')
        heading_label.pack(fill = X)

        # *********************customer details frame************************
        customer_details_frame = LabelFrame(system_frame, text = 'customer details', fg = '#00bfff',
                                            font = ('times new roman', 15, 'bold'),
                                            bg = 'grey20')
        customer_details_frame.pack()

        name_label = Label(customer_details_frame, text = 'Name', font = ('times new roman', 15, 'bold'), bg = 'grey20',
                           fg = 'white')
        name_label.grid(row = 0, column = 0, padx = 25)

        entry_name = Entry(customer_details_frame, bd = 5, font = ('times new roman', 15, 'bold'), fg = 'green')
        entry_name.grid(row = 0, column = 1)

        phone_label = Label(customer_details_frame, text = 'Phone',
                            font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = 'white')
        phone_label.grid(row = 0, column = 2, padx = 25)

        phone_entry = Entry(customer_details_frame, bd = 5, font = ('times new roman', 15, 'bold'), fg = 'green')
        phone_entry.grid(row = 0, column = 3, padx = 10)

        label_bill_number = Label(customer_details_frame, text = 'Bill Number',
                                  font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = 'white')
        label_bill_number.grid(row = 0, column = 4, padx = 25)

        entry_bill_number = Entry(customer_details_frame, bd = 5, font = ('times new roman', 15, 'bold'), fg = 'green')
        entry_bill_number.grid(row = 0, column = 5, padx = 10)

        search_button = Button(customer_details_frame, text = 'Search', font = ('arial', 12, 'bold'), width = 30,
                               bg = '#deb887', command = search)
        search_button.grid(row = 0, column = 6)

        product_frame = Frame(top)
        product_frame.pack()

        # *********************laptop battaries frame************************
        laptop_batterries_frame = LabelFrame(product_frame, text = "Laptop batteries",
                                             font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = '#00bfff')
        laptop_batterries_frame.grid(row = 0, column = 0, padx = 2)

        label_hp_250g6 = Label(laptop_batterries_frame, text = 'Hp 250 G6',
                               font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_250g6.grid(row = 0, column = 0, padx = 20, pady = 8)

        entry_hp_250g6 = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_250g6.grid(row = 0, column = 1, padx = 8, pady = 8)
        entry_hp_250g6.insert(0, '0')

        label_hp_1030g2 = Label(laptop_batterries_frame, text = 'Hp 1030 G2',
                                font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_1030g2.grid(row = 1, column = 0, padx = 20, pady = 8)

        entry_hp_1030g2 = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_1030g2.grid(row = 1, column = 1, padx = 8, pady = 8)
        entry_hp_1030g2.insert(0, '0')

        label_lenovo_x1carbon = Label(laptop_batterries_frame, text = 'Lenovo X1 Carbon',
                                      font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_lenovo_x1carbon.grid(row = 2, column = 0, padx = 20, pady = 8)

        entry_lenovo_x1carbon = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                      fg = 'green')
        entry_lenovo_x1carbon.grid(row = 2, column = 1, padx = 8, pady = 8)
        entry_lenovo_x1carbon.insert(0, '0')

        label_dell_t460s = Label(laptop_batterries_frame, text = 'Dell T460s',
                                 font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_dell_t460s.grid(row = 3, column = 0, padx = 20, pady = 8)

        entry_dell_t460s = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_dell_t460s.grid(row = 3, column = 1, padx = 8, pady = 8)
        entry_dell_t460s.insert(0, '0')

        label_macbook_a1278 = Label(laptop_batterries_frame, text = 'Macbook A1278',
                                    font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_macbook_a1278.grid(row = 4, column = 0, padx = 20, pady = 8)

        entry_macbook_a1278 = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                    fg = 'green')
        entry_macbook_a1278.grid(row = 4, column = 1, padx = 8, pady = 8)
        entry_macbook_a1278.insert(0, '0')

        label_asus = Label(laptop_batterries_frame, text = 'Asus',
                           font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_asus.grid(row = 5, column = 0, padx = 20, pady = 8)

        entry_asus = Entry(laptop_batterries_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_asus.grid(row = 5, column = 1, padx = 8, pady = 8)
        entry_asus.insert(0, '0')

        # *********************laptop keyboards frame************************
        laptop_keyboards_frame = LabelFrame(product_frame, text = 'Laptop keyboards',
                                            font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = '#00bfff')
        laptop_keyboards_frame.grid(row = 0, column = 1, padx = 2)

        label_hp_430g3 = Label(laptop_keyboards_frame, text = 'Hp 430 G3',
                               font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_430g3.grid(row = 0, column = 0, padx = 20, pady = 8)

        entry_hp_430g3 = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_430g3.grid(row = 0, column = 1, padx = 8, pady = 8)
        entry_hp_430g3.insert(0, '0')

        label_macbook_air = Label(laptop_keyboards_frame, text = 'Macbook Air',
                                  font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_macbook_air.grid(row = 1, column = 0, padx = 20, pady = 8)

        entry_macbook_air = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_macbook_air.grid(row = 1, column = 1, padx = 8, pady = 8)
        entry_macbook_air.insert(0, '0')

        label_dell_latitude = Label(laptop_keyboards_frame, text = 'Dell Latitude',
                                    font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_dell_latitude.grid(row = 2, column = 0, padx = 20, pady = 8)

        entry_dell_latitude = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                    fg = 'green')
        entry_dell_latitude.grid(row = 2, column = 1, padx = 8, pady = 8)
        entry_dell_latitude.insert(0, '0')

        label_lenovo_thinkpad = Label(laptop_keyboards_frame, text = 'Lenovo Thinkpad',
                                      font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_lenovo_thinkpad.grid(row = 3, column = 0, padx = 20, pady = 8)

        entry_lenovo_thinkpad = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                      fg = 'green')
        entry_lenovo_thinkpad.grid(row = 3, column = 1, padx = 8, pady = 8)
        entry_lenovo_thinkpad.insert(0, '0')

        label_asus = Label(laptop_keyboards_frame, text = 'Asus',
                           font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_asus.grid(row = 4, column = 0, padx = 20, pady = 8)

        entry_asuss = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_asuss.grid(row = 4, column = 1, padx = 8, pady = 8)
        entry_asuss.insert(0, '0')

        label_hp_9470 = Label(laptop_keyboards_frame, text = 'Hp Folio 9470',
                              font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_9470.grid(row = 5, column = 0, padx = 20, pady = 8)

        entry_hp_9470 = Entry(laptop_keyboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_9470.grid(row = 5, column = 1, padx = 8, pady = 8)
        entry_hp_9470.insert(0, '0')

        # *********************** laptop motherboards frame***************************

        motherboards_frame = LabelFrame(product_frame, text = 'Laptop motherboards',
                                        font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = '#00bfff')
        motherboards_frame.grid(row = 0, column = 2, padx = 2)

        label_hp_820g2 = Label(motherboards_frame, text = 'Hp 820 G2',
                               font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_820g2.grid(row = 0, column = 0, padx = 20, pady = 8)

        entry_hp_820g2 = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_820g2.grid(row = 0, column = 1, padx = 8, pady = 8)
        entry_hp_820g2.insert(0, '0')

        label_lenovo_yoga_11e = Label(motherboards_frame, text = 'Lenovo Yoga 11e',
                                      font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_lenovo_yoga_11e.grid(row = 1, column = 0, padx = 20, pady = 8)

        entry_lenovo_yoga_11e = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_lenovo_yoga_11e.grid(row = 1, column = 1, padx = 8, pady = 8)
        entry_lenovo_yoga_11e.insert(0, '0')

        label_dell_t470 = Label(motherboards_frame, text = 'Dell T470',
                                font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_dell_t470.grid(row = 2, column = 0, padx = 20, pady = 8)

        entry_dell_t470 = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_dell_t470.grid(row = 2, column = 1, padx = 8, pady = 8)
        entry_dell_t470.insert(0, '0')

        label_lenovo_820_revolve = Label(motherboards_frame, text = 'Lenovo 820 revolve',
                                         font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_lenovo_820_revolve.grid(row = 3, column = 0, padx = 20, pady = 8)

        entry_lenovo_820_revolve = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                         fg = 'green')
        entry_lenovo_820_revolve.grid(row = 3, column = 1, padx = 8, pady = 8)
        entry_lenovo_820_revolve.insert(0, '0')

        label_asus = Label(motherboards_frame, text = 'Asus',
                           font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_asus.grid(row = 4, column = 0, padx = 20, pady = 8)

        entry_aasus = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_aasus.grid(row = 4, column = 1, padx = 8, pady = 8)
        entry_aasus.insert(0, '0')

        label_hp_chromebook = Label(motherboards_frame, text = 'Hp Chromebook',
                                    font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_hp_chromebook.grid(row = 5, column = 0, padx = 20, pady = 8)

        entry_hp_chromebook = Entry(motherboards_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_hp_chromebook.grid(row = 5, column = 1, padx = 8, pady = 8)
        entry_hp_chromebook.insert(0, '0')

        # *******************Bill frame*********************************
        bill_frame = Frame(product_frame, bd = 7, relief = GROOVE)
        bill_frame.grid(row = 0, column = 3, padx = 2)
        bill_label = Label(bill_frame, text = "Bill Area", font = ('times new roman', 15, 'bold'), bd = 7,
                           relief = GROOVE)
        bill_label.pack(fill = X)

        scrollbar = Scrollbar(bill_frame, orient = VERTICAL)
        scrollbar.pack(fill = Y, side = RIGHT)

        bill_text_area = Text(bill_frame, height = 14, width = 45, yscrollcommand = scrollbar.set, bg = '#f0f8ff')
        bill_text_area.pack()

        scrollbar.config(command = bill_text_area.yview)

        # ****************************bill menu frame*************************
        bill_menu_frame = LabelFrame(top, text = 'Bill Menu',
                                     font = ('times new roman', 15, 'bold'), bg = 'grey20', fg = '#00bfff')
        bill_menu_frame.pack()

        menu_frame = Frame(bill_menu_frame, bg = 'grey20')
        menu_frame.grid(row = 0, column = 0, pady = 10)
        label_laptop_batteries_price = Label(menu_frame, text = 'Batteries Price',
                                             font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_batteries_price.grid(row = 0, column = 0, padx = 20, pady = 8)

        label_laptop_keyboards_price = Label(menu_frame, text = 'Keyboards Price',
                                             font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_keyboards_price.grid(row = 1, column = 0, padx = 20, pady = 8)

        label_laptop_motherboards_price = Label(menu_frame, text = 'Motherboards Price',
                                                font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_motherboards_price.grid(row = 2, column = 0, padx = 20, pady = 8)

        entry_laptop_batteries_price = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_laptop_batteries_price.grid(row = 0, column = 1, padx = 8, pady = 8)

        entry_laptop_keyboards_price = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_laptop_keyboards_price.grid(row = 1, column = 1, padx = 8, pady = 8)

        entry_laptop_motherboards_price = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'),
                                                fg = 'green')
        entry_laptop_motherboards_price.grid(row = 2, column = 1, padx = 8, pady = 8)

        label_laptop_batteries_tax = Label(menu_frame, text = 'Batteries Tax',
                                           font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_batteries_tax.grid(row = 0, column = 2)

        label_laptop_keyboards_tax = Label(menu_frame, text = 'Keyboards Tax',
                                           font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_keyboards_tax.grid(row = 1, column = 2)

        label_laptop_motherboards_tax = Label(menu_frame, text = 'Kotherboards Tax',
                                              font = ('times new roman', 10, 'bold'), bg = 'grey20', fg = 'white')
        label_laptop_motherboards_tax.grid(row = 2, column = 2)

        entry_laptop_batteries_tax = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_laptop_batteries_tax.grid(row = 0, column = 3, padx = 8, pady = 8)

        entry_laptop_keyboards_tax = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_laptop_keyboards_tax.grid(row = 1, column = 3, padx = 8, pady = 8)

        entry_laptop_motherboards_tax = Entry(menu_frame, bd = 5, font = ('times new roman', 10, 'bold'), fg = 'green')
        entry_laptop_motherboards_tax.grid(row = 2, column = 3, padx = 8, pady = 8)

        # **********************buttons frame****************************
        buttons_frame = Frame(menu_frame, bg = 'grey20')
        buttons_frame.grid(row = 1, column = 5, pady = 10)

        total_button = Button(buttons_frame, text = 'Total',
                              font = ('times new roman', 10, 'bold'), bg = '#ff0000', fg = 'black', height = 3,
                              width = 14,
                              command = total)
        total_button.grid(row = 0, column = 0, padx = 10)

        bill_button = Button(buttons_frame, text = 'Bill',
                             font = ('times new roman', 10, 'bold'), bg = 'yellow', fg = 'black', height = 3,
                             width = 14,
                             command = bill)
        bill_button.grid(row = 0, column = 1, padx = 10)

        email_button = Button(buttons_frame, text = 'Email',
                              font = ('times new roman', 10, 'bold'), bg = '#00ffff', fg = 'black', height = 3,
                              width = 14, command = email)
        email_button.grid(row = 0, column = 2, padx = 10)

        print_button = Button(buttons_frame, text = 'Print',
                              font = ('times new roman', 10, 'bold'), bg = 'blue', fg = 'black', height = 3, width = 14,
                              command = print)
        print_button.grid(row = 0, column = 3, padx = 10)

        clear_button = Button(buttons_frame, text = 'Clear',
                              font = ('times new roman', 10, 'bold'), bg = 'lime green', fg = 'black', height = 3,
                              width = 13, command = clear)
        clear_button.grid(row = 0, column = 4, padx = 10)

        exit_button = Button(buttons_frame, text = 'EXIT',
                             font = ('times new roman', 10, 'bold'), bg = '#663333', fg = 'black', height = 3,
                             width = 13,
                             command = exit)
        exit_button.grid(row = 0, column = 5, padx = 10)

        top.mainloop()


login_window = Tk()
login_window.geometry('1366x768')
login_window.resizable(False, False)
login_window.title('login')

back_ground_image = ImageTk.PhotoImage(file = 'background1.jpg')
background_label = Label(login_window, image = back_ground_image)
background_label.pack()

login_frame = Frame(login_window)
login_frame.place(x = 400, y = 200)

logo_image = PhotoImage(file = 'profile.png')
logo_label = Label(login_frame, image = logo_image)
logo_label.grid(row = 0, column = 1, padx = 20, pady = 20)

user_image = PhotoImage(file = 'user.png')
label_user_name = Label(login_frame, text = 'Username',
                        font = ('times new roman', 20, 'bold'), image = user_image, compound = LEFT)
label_user_name.grid(row = 1, column = 0, pady = 10, padx = 10)

entry_user_name = Entry(login_frame, font = ('times new roman', 20, 'bold'), bd = 5)
entry_user_name.grid(row = 1, column = 1)

password_image = PhotoImage(file = 'password.png')
label_password = Label(login_frame, text = 'Password',
                       font = ('times new roman', 20, 'bold'), image = password_image, compound = LEFT)
label_password.grid(row = 2, column = 0, pady = 10, padx = 10)

entry_password = Entry(login_frame, font = ('times new roman', 20, 'bold'), show = '*', bd = 5)
entry_password.grid(row = 2, column = 1)

button_login = Button(login_frame, text = 'login', bg = 'blue', fg = 'white',
                      font = ('times new roman', 15, 'bold'), width = 10, cursor = 'hand2', command = system_window)
button_login.grid(row = 3, column = 1)

login_window.mainloop()
