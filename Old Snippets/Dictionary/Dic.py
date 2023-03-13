# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 01:06:14 2018

@author: Avis_King
"""

from tkinter import *

from tkinter import messagebox
from tkinter import Menu  

import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def about():
     messagebox.showinfo("About","This is a GUI based dictionary developed by Sivadinesh using Python")


def find():
 word = e.get()
 word = word.lower()
 if word in data:
     if type(data[word]) == list:
         for item in data[word]:
             output = item
             messagebox.showinfo("Synonym for "+word, output)
 elif word.title() in data: 
     if type(data[word.title()]) == list:
         for item in data[word.title()]:
             output = item
             messagebox.showinfo("Synonym for "+word, output)
 elif len(get_close_matches(word, data.keys())) > 0:
     if messagebox.askyesno("Dictionary", "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]) == True:
         word = ("%s" % get_close_matches(word, data.keys())[0])
         if type(data[word]) == list:
             for item in data[word]:
                 output = item
                 messagebox.showinfo("Synonym for "+word, output)
     else:
         messagebox.showwarning("Dictionary", "The word doesn't exist. Please double check it")
 else:
     messagebox.showwarning("Dictionary", "Hope so that the word doesn't exist in the data source")


root = Tk()
root.resizable(0,0)
root.title("Dictionary")
root.geometry("225x90")
root.config(background="#000000")
            
menuBar=Menu(root)  
root.config(menu=menuBar)

menuBar.add_command(label="About", command=about) 
menuBar.add_command(label="Exit", command=root.quit)

        
f=Frame(root,height=280,width=500,bg="#000000")
f.grid(row=0,column=0,padx=10,pady=5)
lab=Label(f,text="Enter your search key ")
lab.grid(row=1,column=0,padx=15,pady=7)
e=Entry(f,width=25)
e.grid(row=2,column=0,padx=1,pady=5)
btn=Button(f,text="Search",command=find)
btn.grid(row=2,column=1,padx=5,pady=7)


root.mainloop()
