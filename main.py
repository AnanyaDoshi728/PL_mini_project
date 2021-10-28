from sqlite3.dbapi2 import connect, register_adapter
import tkinter as tkinter_instance
from tkinter import *
from tkinter import messagebox
import sqlite3
import main_window
import colors


#login window
def render_login_window():
    def on_click_confirm_login():
        try: 
            db_connection = sqlite3.connect("tasks.db")
            db_cursor = db_connection.cursor()
        except Exception as exception:
            messagebox.showerror("Error","Error in connecting to database")

        else:
            try:
                select_record_query = "SELECT * FROM tasks_data WHERE Username=? AND Password=?;"
                db_cursor.execute(select_record_query,(login_username_input.get(),login_password_input.get()))
                record = db_cursor.fetchall()

                if len(record) == 1:
                    #messagebox.showinfo("Login successfull","User authentication succcessfull")
                    global global_username
                    global_username = login_username_input.get()
                    main_window.main_window_render(global_username)
                    


                    """
                    main_window = tkinter_instance.Toplevel()
                    screen_width = main_window.winfo_screenwidth()
                    screen_height = main_window.winfo_screenheight()
                    main_window.geometry(f"{screen_width}x{screen_height}")
                    
                    
                    
                    #l = Label(main_window,text=global_username)
                    #l.pack()
                    
                    #main_window.mainloop()
                    """
              
                   
                else:
                    messagebox.showerror("Login failed","The user does not exsist")
            
            except Exception as exception:
                messagebox.showerror("Exception",exception)
                print(exception)
            
        
    login_window = tkinter_instance.Tk()
    login_window.title("Login")
    login_window.geometry(f"600x450+180+150")
    login_window.resizable(False,False)
    login_window.configure(background=colors.BLACK)

    #create labels
    login_label = Label(login_window,font=FONT_TUPLE_TITLE,text="Login",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    login_username_label = Label(login_window,font=FONT_TUPLE_LABEL,text="Username",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    login_password_label = Label(login_window,font=FONT_TUPLE_LABEL,text="Password",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)

    #create entries
    login_username_input = Entry(login_window,font=FONT_TUPLE_LABEL,width=18)
    login_password_input = Entry(login_window,font=FONT_TUPLE_LABEL,width=18)

    #create buttons 
    confirm_login_button = Button(login_window,font=FONT_TUPLE_LABEL,text="Confirm login",command=on_click_confirm_login,bg=colors.CYAN,fg=colors.BLACK)
    go_to_register_button = Button(login_window,font=FONT_TUPLE_LABEL,text="Go to Register",command=render_signup_window,bg=colors.CYAN,fg=colors.BLACK)

    #place labels
    login_label.place(x=240,y=60)
    login_username_label.place(x=95,y=150)
    login_password_label.place(x=95,y=230)

    #place entries
    login_username_input.place(x=245,y=150)
    login_password_input.place(x=245,y=230)

    #place buttons
    confirm_login_button.place(x=95,y=310)
    go_to_register_button.place(x=300,y=310)


    login_window.mainloop()

def render_signup_window():
    def on_click_confirm_signup():
        #validation
        flag = -1
       
        while flag == -1:
            if username_input.get() == "" or password_input.get() == "" or email_input.get() == "":
                messagebox.showwarning("Empty field(s)","All fields are required")
                break
                    

            elif higher_priority__input.compare("end-1c", "==", "1.0"):
                messagebox.showwarning("Empty tasks","PLease enter some tasks")
                break

            elif lower_priority_input.compare("end-1c","==","1.0"):
                messagebox.showwarning("Empty tasks","PLease enter some tasks")
                break                        
                    
            elif len(username_input.get()) < 8:
                messagebox.showwarning("Invalid username","Username must be atleast 8 charachters")
                break
                    
            elif len(password_input.get()) < 8:
                messagebox.showwarning("Invalid password","Password must be atleast 8 charachters")
                break

            else:
                flag = 0
                    
           #add email validation

       
        if flag == 0:
            try:
                db_connection = sqlite3.connect("tasks.db")
                db_cursor = db_connection.cursor()
            except Exception as exception:
                messagebox.showerror("Error","Could not connect to database")
                print(exception)

            #create table if it does not exsist
            try:
                table_creation_query = "CREATE TABLE IF NOT EXISTS tasks_data (Username text,Password text,Email text,Higher_Priority text,Lower_Priority text);"
                db_cursor.execute(table_creation_query)
                db_connection.commit()

            except Exception as exception:
                messagebox.showerror("Error","Could not create table")
                print(exception)

            

            #check if email or username exsist
            try:
                check_redundancy_query = "SELECT * FROM tasks_data WHERE Username=? OR Email=?;"
                db_cursor.execute(check_redundancy_query,(username_input.get(),email_input.get()))
                redundant_record = db_cursor.fetchall()
                
                #if username or email exsist clear fields
                if len(redundant_record) != 0:
                    messagebox.showerror("Could not create record","The username or email already exsists.Please try again")
                    username_input.delete(0,END)
                    email_input.delete(0,END)
                
            #if username or email doeb not exsist insert data
                else:
                    new_record_insertion_query = "INSERT INTO tasks_data(Username,Password,Email,Higher_Priority,Lower_Priority) VALUES(?,?,?,?,?);"
                    db_cursor.execute(new_record_insertion_query,(username_input.get(),password_input.get(),email_input.get(),higher_priority__input.get(1.0,END),lower_priority_input.get(1.0,END)))
                    db_connection.commit()
                    global global_username
                    global_username = username_input.get()
                    messagebox.showinfo("User created","User successfully created")
                    #insert record and set global variables
                    username_input.delete(0,END)
                    password_input.delete(0,END)
                    email_input.delete(0,END)
                    higher_priority__input.delete("1.0",END)
                    lower_priority_input.delete("1.0",END)
                    print(global_username)


            except Exception as exception:
                messagebox.showerror("Error","New record creation failed")
                print(exception)
        
    

    #window
    signup_window = tkinter_instance.Tk()
    signup_window.title("Sign up")
    signup_window.geometry(f"1100x650+180+150")
    signup_window.configure(background=colors.BLACK)
    signup_window.resizable(False,False)

    #create labels
    username_label = Label(signup_window,font=FONT_TUPLE_LABEL,text="Username",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    password_label = Label(signup_window,font=FONT_TUPLE_LABEL,text="Password",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    email_label = Label(signup_window,font=FONT_TUPLE_LABEL,text="Email",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    tasks_label = Label(signup_window,font=FONT_TUPLE_LABEL_BOLD,text="Tasks",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    higher_priority_label = Label(signup_window,font=FONT_TUPLE_LABEL,text="Higher priority",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)
    lower_priority_label = Label(signup_window,font=FONT_TUPLE_LABEL,text="Lower priority",width=12,anchor="w",bg=colors.BLACK,fg=colors.CYAN)

    #create input fields
    username_input = Entry(signup_window,font=FONT_TUPLE_LABEL,width=18)
    password_input = Entry(signup_window,font=FONT_TUPLE_LABEL,width=18)
    email_input = Entry(signup_window,font=FONT_TUPLE_LABEL,width=18)
    higher_priority__input = Text(signup_window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)
    lower_priority_input = Text(signup_window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)
    
    #create buttons
    signup_button = Button(signup_window,text="Confirm Signup",font=FONT_TUPLE_LABEL,command=on_click_confirm_signup,bg=colors.CYAN,fg=colors.BLACK)
    login_button = Button(signup_window,text="Go To Login",font=FONT_TUPLE_LABEL,command=render_login_window,bg=colors.CYAN,fg=colors.BLACK)

    #place labels
    username_label.place(x=30,y=20)
    password_label.place(x=30,y=100)
    email_label.place(x=30,y=180)
    tasks_label.place(x=552,y=240)
    higher_priority_label.place(x=30,y=300)
    lower_priority_label.place(x=560,y=300)
    
    #place inputs
    username_input.place(x=240,y=20)
    password_input.place(x=240,y=100)
    email_input.place(x=240,y=180)
    higher_priority__input.place(x=240,y=300)
    lower_priority_input.place(x=760,y=300)

    #place buttons
    signup_button.place(x=30,y=550)
    login_button.place(x=280,y=550)    
     
    signup_window.mainloop()

#main

#constanst
FONT_TUPLE_TITLE = ("Helvetica",33)
FONT_TUPLE_LABEL = ("Helvetica",20)
FONT_TUPLE_LABEL_BOLD = ("Helvetica",20,"bold")
FONT_TUPLE_TASK_INPUT = ("Helvetica",15)

#global variable
global global_username 
#global global_password 
#global global_email


initial_window = tkinter_instance.Tk()
initial_window.title("Notes and Tasks")
initial_window.geometry(f"600x450+180+150")
initial_window.resizable(False,False)
initial_window.configure(background=colors.BLACK)

#create labeld and buttons
title_label = Label(initial_window,text="Notes and Tasks",font=FONT_TUPLE_TITLE,bg=colors.BLACK,fg=colors.CYAN)
login_button = Button(initial_window,text="Login",font=FONT_TUPLE_LABEL,height=1,width=7,command=render_login_window,bg=colors.CYAN,fg=colors.BLACK)
signup_button = Button(initial_window,text="Sign up",font=FONT_TUPLE_LABEL,height=1,width=7,command=render_signup_window,bg=colors.CYAN,fg=colors.BLACK)

#place labels and buttons
title_label.place(x=133,y=100)
login_button.place(x=230,y=180)
signup_button.place(x=230,y=260)


initial_window.mainloop()
