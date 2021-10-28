from os import write
import tkinter as tkinter_instance
from tkinter import messagebox
import sqlite3
from tkinter import filedialog
from tkinter import *
from custom_widgets import Dictionary, Wikipedia, translate_widget
from update import update_account, update_task
import colors

FONT_TUPLE_TEXT_AREA = ("Helvetica",15)
FONT_TUPLE_BUTTON = ("Helvetica",18)

def main_window_render(username):

    global is_file_path_open
    is_file_path_open = False

    def new_file():
        global is_file_path_open
        is_file_path_open = False
        main_text_area.delete("1.0",END)

    def open_file():
        main_text_area.delete("1.0",END)
        path_of_file_to_open = filedialog.askopenfilename(title="Open File",filetypes=(("Text Files","*.txt"),))
        opened_file = open(path_of_file_to_open,"r")

        try:
            #check if a file has been selected
            if path_of_file_to_open:
                #set global path to opened file
                global is_file_path_open
                is_file_path_open = path_of_file_to_open
                file_data = opened_file.read()
                main_text_area.insert(END,file_data)
                opened_file.close()

        except Exception as exception:
            messagebox.showerror("Error",exception)
            print(exception)


    def save_as_file():
        path_of_file_to_open = filedialog.asksaveasfilename(defaultextension=".*")
        
        #check if a file is selected
        if path_of_file_to_open:
            opened_file = open(path_of_file_to_open,"w")
            opened_file.write(main_text_area.get(1.0,END))
            opened_file.close()

            
    def save_file():
        global is_file_path_open
        if is_file_path_open:
            opened_file = open(is_file_path_open,'w')
            opened_file.write(main_text_area.get(1.0,END))
            opened_file.close()
            messagebox.showinfo("File saved","File saved successfully")
        
        #if file does not exsist then call save as
        else:
            save_as_file()

    def on_click_dictionary():
        dictionary_instance = Dictionary()

    def on_click_search():
        wikipedia_instance = Wikipedia()

    def on_click_translate():
        translate_widget()

    def highlight_label_and_bind_key(event):
        event.widget.config(bg="white")
        event.widget.focus()
        event.widget.bind("<Key>",trigger_on_key_press)
    
        

    def trigger_on_key_press(event):
        key_pressed = event.char
        if key_pressed.lower() == "a":
            update_account(username)
        if key_pressed.lower() == "t":
            update_task(username)
        update_record_label.config(bg="grey")
        main_window.focus_set()


    def on_click_view_tasks(main_username):
        try: 
            db_connection = sqlite3.connect("tasks.db")
            db_cursor = db_connection.cursor()
        except Exception as exception:
            messagebox.showerror("Error","Error in connecting to database")
        
        else:
            try: 
                db_cursor.execute("SELECT * FROM tasks_data WHERE Username=?",(main_username,))
                #db_cursor.execute(display_record_query)
                #[('nobara', 'strayDoll', 'nobara@gmail.com', 'make jujustu and study notes\n', 'make movie list\n')]
                record = db_cursor.fetchall()
                
                window = tkinter_instance.Toplevel()
                window.geometry(f"600x580+180+150")
                window.title("View tasks")
                window.resizable(False,False)
                window.configure(background=colors.BLACK)

                #create labels
                higher_priority_label = Label(window,font=FONT_TUPLE_TEXT_AREA,text="Higher priority",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)
                lower_priority_label = Label(window,font=FONT_TUPLE_TEXT_AREA,text="Lower priority",width=12,anchor="w",fg=colors.GREEN,bg=colors.BLACK)

                #create text area
                higher_priority_input = Text(window,font=FONT_TUPLE_TEXT_AREA,width=27,height=8)
                lower_priority_input = Text(window,font=FONT_TUPLE_TEXT_AREA,width=27,height=8)

                higher_priority_input.insert(1.0,record[0][3])
                lower_priority_input.insert(1.0,record[0][4])

                higher_priority_input.configure(state=DISABLED)
                lower_priority_input.configure(state=DISABLED)

                #place labels
                higher_priority_label.place(x=30,y=30)
                lower_priority_label.place(x=30,y=290)

                #place text area
                higher_priority_input.place(x=235,y=30)
                lower_priority_input.place(x=235,y=290)


                window.mainloop()


            except Exception as exception:
                print(f"Exception: {exception}")
                messagebox.showerror("Error","Could not display record")
        
        

    main_window = tkinter_instance.Tk()
    main_window.title("Notes") #Change to top level and put into function
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f"{screen_width}x{screen_height}")
    main_window.configure(background=colors.BLACK)

    #frame
    main_frame = Frame(main_window)

    #scrollbars
    vertical_scrollbar = Scrollbar(main_frame)
    vertical_scrollbar.pack(side=RIGHT,fill=Y)
    horizontal_scrollbar = Scrollbar(main_frame,orient="horizontal")
    horizontal_scrollbar.pack(side=BOTTOM,fill="x")

    #text_area
    main_text_area = Text(main_frame,width=100,height=27,font=FONT_TUPLE_TEXT_AREA,yscrollcommand=vertical_scrollbar.set,wrap=NONE,xscrollcommand=horizontal_scrollbar.set)
    main_text_area.pack()

    #configure scrollbar
    vertical_scrollbar.config(command=main_text_area.yview)
    horizontal_scrollbar.config(command=main_text_area.xview)

    #create menu
    main_window_menu = Menu(main_window)

    #file menu
    file_menu = Menu(main_window_menu,tearoff=0,font=FONT_TUPLE_TEXT_AREA)
    file_menu.add_command(label="New",command=new_file,font=FONT_TUPLE_TEXT_AREA)
    file_menu.add_command(label="Open",command=open_file,font=FONT_TUPLE_TEXT_AREA)
    file_menu.add_command(label="Save",command=save_file,font=FONT_TUPLE_TEXT_AREA)
    file_menu.add_command(label="Save As",command=save_as_file,font=FONT_TUPLE_TEXT_AREA)
    main_window_menu.add_cascade(label="File",menu=file_menu,font=FONT_TUPLE_TEXT_AREA)

    #configure menu
    file_menu.config(font=FONT_TUPLE_TEXT_AREA)
    main_window.config(menu=main_window_menu)

    #create buttons
    dictionary_button = Button(main_window,text="Dictionary",font=FONT_TUPLE_BUTTON,width=10,command=on_click_dictionary,bg=colors.GREEN,fg=colors.BLACK)
    search_button = Button(main_window,text="Search",font=FONT_TUPLE_BUTTON,width=10,command=on_click_search,bg=colors.GREEN,fg=colors.BLACK)
    translate_button = Button(main_window,text="Translate",font=FONT_TUPLE_BUTTON,width=10,command=on_click_translate,bg=colors.GREEN,fg=colors.BLACK)
    view_tasks_button = Button(main_window,text="View tasks",font=FONT_TUPLE_BUTTON,width=10,command=lambda:on_click_view_tasks(username),bg=colors.GREEN,fg=colors.BLACK)

    #labels
    update_record_label = Label(main_window,text="Select this text and press: ",font=FONT_TUPLE_TEXT_AREA,fg=colors.GREEN,bg=colors.BLACK)
    update_profile_label = Label(main_window,text="A to update profile",font=FONT_TUPLE_TEXT_AREA,fg=colors.GREEN,bg=colors.BLACK)
    update_tasks_label = Label(main_window,text="T to update tasks",font=FONT_TUPLE_TEXT_AREA,fg=colors.GREEN,bg=colors.BLACK)


    #key bindings
    update_record_label.bind("<Button-1>",highlight_label_and_bind_key)

    #place widgets
    main_frame.place(x=30,y=30)
    dictionary_button.place(x=30,y=700)
    search_button.place(x=240,y=700)
    translate_button.place(x=450,y=700)
    view_tasks_button.place(x=660,y=700)

    update_record_label.place(x=1220,y=50)
    update_profile_label.place(x=1220,y=110)
    update_tasks_label.place(x=1220,y=170)
                        
    main_window.mainloop()
