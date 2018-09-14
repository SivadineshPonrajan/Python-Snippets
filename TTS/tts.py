# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 00:40:07 2018

@author: Avis_King
"""

import win32com.client as wincl
from tkinter import *


def text2Speech():
 text = e.get()
 speak = wincl.Dispatch("SAPI.SpVoice")
 speak.Speak(text)

tts = Tk()
tts.resizable(0,0)
tts.title("Text to Speech")
tts.geometry("225x110")
tts.config(background="#000000")
           
f=Frame(tts,height=280,width=500,bg="#000000")
f.grid(row=0,column=0,padx=10,pady=5)
lab=Label(f,text="Enter your Text below")
lab.grid(row=1,column=0,padx=10,pady=7)
e=Entry(f,width=30)
e.grid(row=2,column=0,padx=10,pady=5)
btn=Button(f,text="Speak",command=text2Speech)
btn.grid(row=3,column=0,padx=20,pady=7)
tts.mainloop()
