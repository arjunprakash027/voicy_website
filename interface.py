import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile
import os
from converter import convert_to_speech
from credentials import *
from delete_file import *

my_w = tk.Tk()
my_w.geometry("410x300")  # Size of the window 
my_w.title('voicy')
my_font1=('times', 18, 'bold')
T = Text(my_w, height = 5, width = 52)
T2 =Text(my_w, height = 5, width = 52)
l1 = tk.Label(my_w,text='Upload text files',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload Files', 
   width=20,command = lambda:upload_file())
b2 = tk.Button(my_w, text='convert to speech', 
   width=20,command = lambda:convert_speech())
b1.grid(row=2,column=1,columnspan=4)
b2.grid(row=4,column=1,columnspan=4)

def upload_file():
    delete_files()
    f_types = [('text Files', '*.txt')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    T.grid(row=100,column=1,columnspan=20)
    if filename == "":
        T.insert(tk.END, "upload stopped \n")
    else:
        for entry in filename:
            T.insert(tk.END, "uploaded {} \n".format(os.path.split(entry)[1]))
        
    for entry in filename:
        f = open("{}".format(entry), "r")
        text = ('''{}'''.format(f.read()))
        file = open("text_files/{}".format(os.path.split(entry)[1]), 'w')
        file.write(text)
        file.close() 

def convert_speech():
    content = {}
    entries = os.listdir('text_files/')
    for entry in entries:
        f = open("text_files/{}".format(entry), "r")
        text = ('''{}'''.format(f.read()))
        content[entry] = text
    create_apikey()
    for i in range (len(list(content))):
        filename = list(content)[i]
        text = list(content.values())[i]
        convert_to_speech(text,filename)
        T.grid(row=100,column=1,columnspan=20)
        T.insert(tk.END, "converted {} to speech!! \n".format(filename))
    os.remove("ai-learning-text-to-speech-93061333450a.json")           
# Keep the window open
my_w.mainloop()  



#curr_directory = os.getcwd()
#print("{}/text_files".format(curr_directory))