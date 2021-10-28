import tkinter as tkinter_instance
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import requests
import json
import wikipedia
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import colors

FONT_TUPLE_TEXT = ("Helvetica",15)
FONT_TUPLE_TASK_INPUT = ("Helvetica",15)
FONT_TUPLE_LABEL = ("Helvetica",18)


class Dictionary():
    def __init__(self):
        self.window = tkinter_instance.Toplevel()
        self.window.title("Dictionary")
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.configure(background=colors.BLACK)

        
        self.input_label = Label(self.window,font=("Helvetica",15),text="Enter a word:",bg=colors.BLACK,fg=colors.GREEN)
        self.input_word = Entry(self.window,font=("Helvetica",15),width=23)
        self.find_image = Image.open("research.png")
        self.find_image = self.find_image.resize((60,60),Image.ANTIALIAS)
        self.final_find_image = ImageTk.PhotoImage(self.find_image)
        self.find_button = Button(self.window,image=self.final_find_image,borderwidth=0,command=self.find_meaning_of_word,bg=colors.BLACK)

        self.entered_word_label = Label(self.window,text="",bg=colors.BLACK)
        self.word_type_label = Label(self.window,text="",bg=colors.BLACK)
        self.word_definition_label = Label(self.window,text="",bg=colors.BLACK)
        self.example_sentece_label = Label(self.window,text="",bg=colors.BLACK)

        
        self.input_label.place(x=50,y=40)
        self.input_word.place(x=230,y=40)
        self.find_button.place(x=510,y=40)

        self.entered_word_label.place(x=50,y=120)
        self.word_type_label.place(x=50,y=210)
        self.word_definition_label.place(x=50,y=300)
        self.example_sentece_label.place(x=50,y=390)

        self.window.mainloop()
    
    def find_meaning_of_word(self):
        

        word = self.input_word.get()

        dictionary_api_url = f"https://owlbot.info/api/v4/dictionary/{word}"

        dictionary_api_header = { "Authorization": "Token 9a6994984f27d6f2289e775b208622f996f8dc0b"}

        try:
            dictionary_api_response = requests.get(dictionary_api_url,headers=dictionary_api_header)
            response_content = json.loads(dictionary_api_response.content)

            entered_word = response_content["word"]
            word_type = response_content["definitions"][0]["type"]
            word_definition = response_content["definitions"][0]["definition"]
            example_sentece = response_content["definitions"][0]["example"]

            
        
        except Exception as exception:
            messagebox.showerror("Error","Could not find meaning of word")

        else:
            self.entered_word_label.config(text=f"Word: {entered_word}",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)
            self.word_type_label.config(text=f"Type: {word_type}",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)
            self.word_definition_label.config(text=f"Definition: {word_definition}",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)
            self.example_sentece_label.config(text=f"Example: {example_sentece}",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)


            
class Wikipedia():
    def __init__(self):
        self.window = tkinter_instance.Toplevel()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.title("Search")
        self.window.configure(background=colors.BLACK)

        self.search_label = Label(self.window,text="Search: ",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)
        self.search_input = Entry(self.window,font=("Helvetica",18),width=23)
        self.lines_label = Label(self.window,text="Lines: ",font=("Helvetica",18),bg=colors.BLACK,fg=colors.GREEN)
        self.lines_input = Entry(self.window,font=("Helvetica",18),width=8)

        self.find_image = Image.open("research.png")
        self.find_image = self.find_image.resize((60,60),Image.ANTIALIAS)
        self.final_find_image = ImageTk.PhotoImage(self.find_image)
        self.find_button = Button(self.window,image=self.final_find_image,borderwidth=0,command=self.on_click_search,bg=colors.BLACK)
        
        #text frame
        self.output_frame= Frame(self.window)

        #scrollbars
        self.vertical_scrollbar = Scrollbar(self.output_frame)
        self.vertical_scrollbar.pack(side=RIGHT,fill=Y)
        #text_area
        self.main_text_area = Text(self.output_frame,width=120,height=27,font=FONT_TUPLE_TEXT,yscrollcommand=self.vertical_scrollbar.set,bg=colors.BLACK,fg=colors.CYAN)
        self.main_text_area.pack()

        #configure scrollbar
        self.vertical_scrollbar.config(command=self.main_text_area.yview)

        self.search_label.place(x=50,y=40)
        self.search_input.place(x=160,y=40)
        self.lines_label.place(x=500,y=40)
        self.lines_input.place(x=580,y=40)
        self.find_button.place(x=700,y=40)

        self.output_frame.place(x=50,y=130)


        self.window.mainloop()
        
    def on_click_search(self):
        self.main_text_area.delete("1.0",END)
        search = self.search_input.get()
        lines = self.lines_input.get()

        try:
            summary = wikipedia.summary(search,int(lines))
        except Exception as exception:
            messagebox.showerror("Error","Could not find data")
            print(exception)
        else:
            self.main_text_area.insert(1.0,summary)
            

def translate_widget():
    def on_click_translate():
        input_text = source_text.get(1.0,END)
        source_text.delete("1.0",END)
        destination_text.delete("1.0",END)
        try:
            url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/8d1a4a9b-e104-4cea-87ea-910a9eac0356";
            api_key = "pZKPRVEouNEuGcP3Dmh9zwrT2pNHWXh8Vk1np6Tc8xCW"

            authenticator=IAMAuthenticator(api_key)
            lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
            lt.set_service_url(url)

            #Translate
            #translation=lt.translate(text='Hello World',model_id='en-de').get_result()
            #print(translation['translations'][0]['translation'])

            #English
            if source_language_var.get() == "English":

                if destination_language_var.get() == "French":
                    translation=lt.translate(text=input_text,model_id='en-fr').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "German":
                    translation=lt.translate(text=input_text,model_id='en-de').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Italian":
                    translation=lt.translate(text=input_text,model_id='en-it').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Spanish":
                    translation=lt.translate(text=input_text,model_id='en-es').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "English":
                    destination_text.insert(1.0,input_text)
            
            #Spanish
            if source_language_var.get() == "Spanish":

                if destination_language_var.get() == "French":
                    translation=lt.translate(text=input_text,model_id='es-fr').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "German":
                    translation=lt.translate(text=input_text,model_id='es-de').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Italian":
                    translation=lt.translate(text=input_text,model_id='es-it').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "English":
                    translation=lt.translate(text=input_text,model_id='es-en').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Spanish":
                    destination_text.insert(1.0,input_text)

            #German
            if source_language_var.get() == "German":

                if destination_language_var.get() == "French":
                    translation=lt.translate(text=input_text,model_id='de-fr').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Spanish":
                    translation=lt.translate(text=input_text,model_id='de-es').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Italian":
                    translation=lt.translate(text=input_text,model_id='de-it').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "English":
                    translation=lt.translate(text=input_text,model_id='de-en').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "German":
                    destination_text.insert(1.0,input_text)
        
            #French
            if source_language_var.get() == "French":

                if destination_language_var.get() == "German":
                    translation=lt.translate(text=input_text,model_id='fr-de').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Spanish":
                    translation=lt.translate(text=input_text,model_id='fr-es').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Italian":
                    translation=lt.translate(text=input_text,model_id='fr-it').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "English":
                    translation=lt.translate(text=input_text,model_id='fr-en').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "French":
                    destination_text.insert(1.0,input_text)
        
            #Italian
            if source_language_var.get() == "Italian":

                if destination_language_var.get() == "German":
                    translation=lt.translate(text=input_text,model_id='it-fr').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Spanish":
                    translation=lt.translate(text=input_text,model_id='it-es').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "French":
                    translation=lt.translate(text=input_text,model_id='it-fr').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "English":
                    translation=lt.translate(text=input_text,model_id='it-en').get_result()
                    destination_text.insert(1.0,translation['translations'][0]['translation'])

                if destination_language_var.get() == "Italian":
                    destination_text.insert(1.0,input_text)
        

        except Exception as exception:
            messagebox.showerror("Error",exception)
            print(exception)
            
    

    window = tkinter_instance.Toplevel()
    window.geometry("600x630")
    window.title("Translator")
    window.resizable(False,False)
    window.configure(background=colors.BLACK)
    

    #labels
    source_language_label = Label(window,text="Source language: ",font=FONT_TUPLE_LABEL,bg=colors.BLACK,fg=colors.GREEN)
    destination_language_label  =Label(window,text="Destination language: ",font=FONT_TUPLE_LABEL,bg=colors.BLACK,fg=colors.GREEN)

    #drop down menus
    source_language_var = StringVar()
    destination_language_var = StringVar()

    source_language_list = ["English","Spanish","French","German","Italian"]
    destination_language_list = ["Spanish","English","French","German","Italian"]

    source_language_dropdown_menu = OptionMenu(window,source_language_var,*source_language_list)
    destination_language_dropdown_menu  = OptionMenu(window,destination_language_var,*destination_language_list)

    source_language_dropdown_menu.config(font=FONT_TUPLE_LABEL,bg=colors.GREEN,fg=colors.BLACK)
    source_language_var.set(source_language_list[0])
    source_language_menu = window.nametowidget(source_language_dropdown_menu.menuname)
    source_language_menu.config(font=FONT_TUPLE_LABEL,bg=colors.GREEN,fg=colors.BLACK)

    destination_language_dropdown_menu.config(font=FONT_TUPLE_LABEL,bg=colors.GREEN,fg=colors.BLACK)
    destination_language_var.set(destination_language_list[0])
    destination_language_menu = window.nametowidget(destination_language_dropdown_menu.menuname)
    destination_language_menu.config(font=FONT_TUPLE_LABEL,bg=colors.GREEN,fg=colors.BLACK)


    #text areas
    source_text = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)
    destination_text = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)

    #button
    translate_button = Button(window,font=FONT_TUPLE_LABEL,command=on_click_translate,text="Translate",bg=colors.GREEN,fg=colors.BLACK)

    #place
    source_language_label.place(x=30,y=30)
    source_language_dropdown_menu.place(x=240,y=30)

    destination_language_label.place(x=30,y=300)
    destination_language_dropdown_menu.place(x=280,y=300)

    source_text.place(x=240,y=90)
    destination_text.place(x=240,y=360)

    translate_button.place(x=420,y=570)

    window.mainloop()