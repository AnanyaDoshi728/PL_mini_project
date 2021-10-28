import tkinter as tkinter_instance
from tkinter import *
from tkinter import messagebox
import sqlite3
import colors

FONT_TUPLE_LABEL = ("Helvetica",18)
FONT_TUPLE_TASK_INPUT = ("Helvetica",15)

#put in function
def update_account(username):
    print(username)

    def on_click_update():
        try: 
            db_connection = sqlite3.connect("tasks.db")
            db_cursor = db_connection.cursor()
        except Exception as exception:
            messagebox.showerror("Error","Error in connecting to database")

        else:
            try:
                db_cursor.execute("UPDATE tasks_data SET Username=?,Password=?,Email=? WHERE Username=?",(update_username_input.get(),update_password_input.get(),update_email_input.get(),username))
                db_connection.commit()
                messagebox.showinfo("Updated","Record updated")

            except Exception as exception:
                messagebox.showerror("Error",exception)
                print(exception)

        

    window = tkinter_instance.Toplevel()
    window.title("Update account")
    window.geometry(f"600x450+180+150")
    window.resizable(False,False)
    window.configure(background=colors.BLACK)

    #create labels
    update_username_label = Label(window,font=FONT_TUPLE_LABEL,text="Username",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)
    update_password_label = Label(window,font=FONT_TUPLE_LABEL,text="Password",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)
    update_email_label = Label(window,font=FONT_TUPLE_LABEL,text="Email",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)

    #create inputs
    update_username_input = Entry(window,font=FONT_TUPLE_LABEL,width=18)
    update_password_input = Entry(window,font=FONT_TUPLE_LABEL,width=18)
    update_email_input = Entry(window,font=FONT_TUPLE_LABEL,width=18)

    #create button
    update_button = Button(window,font=FONT_TUPLE_LABEL,text="Update",width=8,command=on_click_update,bg=colors.GREEN,fg=colors.BLACK)

    #place labels
    update_username_label.place(x=95,y=60)
    update_password_label.place(x=95,y=150)
    update_email_label.place(x=95,y=230)

    #place input
    update_username_input.place(x=245,y=60)
    update_password_input.place(x=245,y=150)
    update_email_input.place(x=245,y=230)

    #place button
    update_button.place(x=367,y=310)


    window.mainloop()



def update_task(username):

    def on_click_update():
        try: 
            db_connection = sqlite3.connect("tasks.db")
            db_cursor = db_connection.cursor()
        except Exception as exception:
            messagebox.showerror("Error","Error in connecting to database")

        else:
            try:
                db_cursor.execute("UPDATE tasks_data SET Higher_Priority=?,Lower_Priority=? WHERE Username=?",(higher_priority_input.get(1.0,END),lower_priority_input.get(1.0,END),username))
                db_connection.commit()
                messagebox.showinfo("Updated","Record updated")

            except Exception as exception:
                messagebox.showerror("Error",exception)
                print(exception)


    window = tkinter_instance.Toplevel()
    window.title("Update task")
    window.geometry(f"600x600+180+150")
    window.resizable(False,False)
    window.configure(background=colors.BLACK)

    #create labels
    higher_priority_label = Label(window,font=FONT_TUPLE_LABEL,text="Higher priority",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)
    lower_priority_label = Label(window,font=FONT_TUPLE_LABEL,text="Lower priority",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)


    #create text area
    higher_priority_input = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)
    lower_priority_input = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)

    #create button
    update_button = Button(window,font=FONT_TUPLE_LABEL,text="Update",width=8,command=on_click_update,bg=colors.GREEN,fg=colors.BLACK)

    #place labels
    higher_priority_label.place(x=30,y=30)
    lower_priority_label.place(x=30,y=290)

    #place text area
    higher_priority_input.place(x=235,y=30)
    lower_priority_input.place(x=235,y=290)

    #place button
    update_button.place(x=410,y=510)

    window.mainloop()

