# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 01:06:14 2018

@author: Avis_King
"""

import os
from tkinter import *
from tkinter import messagebox
from tkinter import Menu  

device = ""
doom = ""
one = "netsh interface ip set address \""+device+"\" static 172.16.16."+doom+" 255.255.255.0 172.16.16.1"
two = "netsh interface ip set dns \""+device+"\" static 8.8.8.8"
resetone = "netsh interface ip set address \""+device+"\" dhcp"
resettwo = "netsh interface ip set dns \""+device+"\" dhcp"

def about():
     messagebox.showinfo("About","This GUI based network configurator was developed by Sivadinesh")

def sel():
	selection = "You selected the option " + str(val.get()) + str(e.get())
	if (val.get()==1):
		device = "Ethernet"
		doom = str(e.get())
		if(doom.isdigit() and int(doom)<=255):
			one = "netsh interface ip set address \""+device+"\" static 172.16.16."+doom+" 255.255.255.0 172.16.16.1"
			two = "netsh interface ip set dns \""+device+"\" static 8.8.8.8"
			# messagebox.showinfo(one, one+two)
			os.system(one)
			os.system(two)
		else:
			messagebox.showwarning("Warning", "Invalid Wi-Fi Id")
		pass
	elif (val.get()==2):
		device = "Wi-Fi"
		doom = str(e.get())
		if(doom.isdigit() and int(doom)<=255):
			one = "netsh interface ip set address \""+device+"\" static 172.16.16."+doom+" 255.255.255.0 172.16.16.1"
			two = "netsh interface ip set dns \""+device+"\" static 8.8.8.8"
			# messagebox.showinfo(one, one+two)
			os.system(one)
			os.system(two)
		else:
			messagebox.showwarning("Warning", "Invalid Wi-Fi Id")
		pass
	elif (val.get()==3):
		device = str(e0.get())
		if (device==""):
			messagebox.showwarning("Warning", "Invalid NIC Card")
			pass
		else:
			doom = str(e.get())
			if(doom.isdigit() and int(doom)<=255):
				one = "netsh interface ip set address \""+device+"\" static 172.16.16."+doom+" 255.255.255.0 172.16.16.1"
				two = "netsh interface ip set dns \""+device+"\" static 8.8.8.8"
				# messagebox.showinfo(one, one+two)
				os.system(one)
				os.system(two)
			else:
				messagebox.showwarning("Warning", "Invalid Wi-Fi Id")
			pass
		pass
	else:
		messagebox.showwarning("Warning", "Invalid selection")


def reset():
	if (val.get()==1):
		device = "Ethernet"
		resetone = "netsh interface ip set address \""+device+"\" dhcp"
		resettwo = "netsh interface ip set dns \""+device+"\" dhcp"
		# messagebox.showinfo("hello", resetone+resettwo)
		os.system(resetone)
		os.system(resettwo)
		pass
	elif (val.get()==2):
		device = "Wi-Fi"
		resetone = "netsh interface ip set address \""+device+"\" dhcp"
		resettwo = "netsh interface ip set dns \""+device+"\" dhcp"
		# messagebox.showinfo("hello", resetone+resettwo)
		os.system(resetone)
		os.system(resettwo)
		pass
	elif (val.get()==3):
		device = str(e0.get())
		if (device==""):
			messagebox.showwarning("Warning", "Invalid NIC Card")
			pass
		else:
			resetone = "netsh interface ip set address \""+device+"\" dhcp"
			resettwo = "netsh interface ip set dns \""+device+"\" dhcp"
			# messagebox.showinfo("hello", resetone+resettwo)
			os.system(resetone)
			os.system(resettwo)
			pass
		pass
	else:
		messagebox.showwarning("Warning", "Invalid selection")

def find():
	messagebox.showinfo("Configuration", word)


root = Tk()
root.resizable(0,0)
root.title("Network Configurator")
root.geometry("370x250")
root.config(background="#000000")
            
menuBar=Menu(root) 
root.config(menu=menuBar)

menuBar.add_command(label="About", command=about)
menuBar.add_command(label="Exit", command=root.quit)

f0=Frame(root,height=30,width=400,bg="#000000")
f0.grid(row=0,column=0,padx=0,pady=5)
f=Frame(root,height=80,width=400,bg="#000000")
f.grid(row=1,column=0,padx=10,pady=5)
val = IntVar()
R1 = Radiobutton(f0, text="Ethernet", variable=val, value=1,fg="#ffffff",bg="#000000",selectcolor="#fb8c00")
R1.grid(row=0,column=0)
R2 = Radiobutton(f0, text="Wi-Fi", variable=val, value=2,fg="#ffffff",bg="#000000",selectcolor="#fb8c00")
R2.grid(row=0,column=1)
R3 = Radiobutton(f0, text="Other", variable=val, value=3,fg="#ffffff",bg="#000000",selectcolor="#fb8c00")
R3.grid(row=0,column=2)
e0=Entry(f0,width=25)
e0.grid(row=0,column=3,padx=1,pady=5)
lab=Label(f,text="Enter your team's Wi-fi id ",bg="#111",fg="#ffffff")
lab.grid(row=1,column=0,padx=15,pady=35)
e=Entry(f,width=25)
e.grid(row=1,column=1,padx=1,pady=5)
btn1=Button(f,text="Modify",width=20,height=3,bg="#fb8c00",command=sel)
btn1.grid(row=2,column=0,padx=5,pady=7)
btn2=Button(f,text="Reset",width=20,height=3,bg="#fb8c00",command=reset)
btn2.grid(row=2,column=1,padx=5,pady=7)

root.mainloop()