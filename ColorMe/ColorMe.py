# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:29:12 2018

@author: Avis_King
"""

# import the modules 
import tkinter
from tkinter import Menu  
from tkinter import messagebox
import random
 
# total colours
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score = 0
 
# totally 30 seconds
timeleft = 30
 
# start the game (main function)
def startGame(event):
    if timeleft == 30:
         
        # timer
        countdown()

    # next colour.
    nextColour()
 

def nextColour():
 
    # global declaration
    global score
    global timeleft
 
    if timeleft > 0:
 
        # make the text entry box active.
        e.focus_set()
 
        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
             
            score += 1
 
        # clear the text entry box.
        e.delete(0, tkinter.END)
         
        random.shuffle(colours)
         
        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
         
        # update the score
        scoreLabel.config(text = "Score: " + str(score))
 
def about():
     messagebox.showinfo("About!!!","ColorMe is a game developed by Sivadinesh using Python")

    

def countdown():
 
    global timeleft
 
    if timeleft > 0:

        timeleft -= 1
         
        # update the time left label
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
                                
        # run the function again after 1 second
        timeLabel.after(1000, countdown)
        
    elif timeleft <= 0:
        messagebox.showinfo("Gameover!!!","Good Try!!! "+"Your Score is  " + str(score))
 
 
# Driver Code
 
# create a GUI window
root = tkinter.Tk()
 
# set the title
root.title("ColorMe")
 
# set the size
root.geometry("375x200")

# menubar create
menuBar=Menu(root)  
root.config(menu=menuBar)

# menubar Menu
msgMenu=Menu(menuBar, tearoff=0)  
msgMenu.add_command(label="About ColorMe", command=about)
menuBar.add_cascade(label="More", menu=msgMenu)    
 
# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour"
                        " of the words, and not the word text!",
                                      font = ('Roboto', 12))
instructions.pack() 
 
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Roboto', 12))
scoreLabel.pack()
 
# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Roboto', 12))
               
timeLabel.pack()
 
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Roboto', 60))
label.pack()
 
# add a text entry box for
# typing in colours
e = tkinter.Entry(root)
 
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
 
# set focus on the entry box
e.focus_set()
 
# start the GUI
root.mainloop()