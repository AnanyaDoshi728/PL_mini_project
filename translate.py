
import tkinter as tkinter_instance
from tkinter import *
from tkinter import messagebox
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

FONT_TUPLE_LABEL = ("Helvetica",18)
FONT_TUPLE_TASK_INPUT = ("Helvetica",15)


"""


url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/8d1a4a9b-e104-4cea-87ea-910a9eac0356";
api_key = "pZKPRVEouNEuGcP3Dmh9zwrT2pNHWXh8Vk1np6Tc8xCW"

authenticator=IAMAuthenticator(api_key)
lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
lt.set_service_url(url)
#Translate
translation=lt.translate(text='Hello World',model_id='en-de').get_result()
print(translation['translations'][0]['translation'])

"""

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
        
   

window = tkinter_instance.Tk()
window.geometry("600x630")

#labels
source_language_label = Label(window,text="Source language: ",font=FONT_TUPLE_LABEL)
destination_language_label  =Label(window,text="Destination language: ",font=FONT_TUPLE_LABEL)

#drop down menus
source_language_var = StringVar()
destination_language_var = StringVar()

source_language_list = ["English","Spanish","French","German","Italian"]
destination_language_list = ["Spanish","English","French","German","Italian"]

source_language_dropdown_menu = OptionMenu(window,source_language_var,*source_language_list)
destination_language_dropdown_menu  = OptionMenu(window,destination_language_var,*destination_language_list)

source_language_dropdown_menu.config(font=FONT_TUPLE_LABEL)
source_language_var.set(source_language_list[0])
source_language_menu = window.nametowidget(source_language_dropdown_menu.menuname)
source_language_menu.config(font=FONT_TUPLE_LABEL)

destination_language_dropdown_menu.config(font=FONT_TUPLE_LABEL)
destination_language_var.set(destination_language_list[0])
destination_language_menu = window.nametowidget(destination_language_dropdown_menu.menuname)
destination_language_menu.config(font=FONT_TUPLE_LABEL)


#text areas
source_text = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)
destination_text = Text(window,font=FONT_TUPLE_TASK_INPUT,width=27,height=8)

#button
translate_button = Button(window,font=FONT_TUPLE_LABEL,command=on_click_translate,text="Translate")

#place
source_language_label.place(x=30,y=30)
source_language_dropdown_menu.place(x=240,y=30)

destination_language_label.place(x=30,y=300)
destination_language_dropdown_menu.place(x=280,y=300)

source_text.place(x=240,y=90)
destination_text.place(x=240,y=360)

translate_button.place(x=420,y=570)

window.mainloop()