#GSH -GUI openSSH interface - version 1.0 as of October 22, 2019. Written and maintained by Joe Diamond.
#Contact him at jdiamond_11@comcast.net or at the github repo: https://gihub.com/joebass85/GSH
import tkinter as tki
from subprocess import Popen
import pyautogui as pyag
from time import sleep
#variable creation
name = ''
ip = ''
port = ''
key = ''
term = ''
#environment variables
master = tki.Tk()
master.title("GSH Program - gui ssh in Python")
master.resizable(False,False)
master.geometry('600x100')
#username entry-box
ent = tki.Entry(master)
ent.grid(row=0, column=1)
def name_get():
    global name
    name = ent.get()
#username label
username = tki.Label(master, text="Username:")
username.grid(row=0, column=0)
#Destination IP label
dest = tki.Label(master, text="Destination:")
dest.grid(row=0, column=3)
#Destination IP entry-box
destEnt = tki.Entry(master)
destEnt.grid(row=0, column=4)
def IP_get():
    global ip
    ip = destEnt.get()
#Port nuber label
ports = tki.Label(master, text="Port:")
ports.grid(row=1, column=3)
#Port number entry-box
portEnt = tki.Entry(master)
portEnt.grid(row=1, column=4)
def port_get():
     global port
     port = portEnt.get()
#ssh key location textbox
key = tki.Label(master, text="Key Location:")
key.grid(row=1,column=0)
#ssh key entry-box
keyEnt = tki.Entry(master)
keyEnt.grid(row=1,column=1)
def key_get():
     global key
     key = keyEnt.get()
#terminal name textbox
term = tki.Label(master, text="Terminal Name:")
term.grid(row=2,column=0)
#terminal name entry-box
termEnt = tki.Entry(master)
termEnt.grid(row=2,column=1)
def term_get():
     global term
     term = termEnt.get()
def mainfunc ():
    if key != '' and port != '':
		    Popen([term])
		    sleep(3)
		    pyag.typewrite("ssh " + name + "@" + ip + " -p " + port + " -i " + key)
		    pyag.press("return")
    if key != '' and port == '':
		    Popen([term])
		    sleep(3)
		    pyag.typewrite("ssh " + name + "@" + ip + " -i " + key)
		    pyag.press("return")
    if port != '' and key == '':
		    Popen([term])
		    sleep(3)
		    pyag.typewrite("ssh " + name + "@" + ip + " -p " + port)
		    pyag.press("return")
    if port == '' and key == '':
		    Popen([term])
		    sleep(3)
		    pyag.typewrite("ssh " + name + "@" + ip)
		    pyag.press("return")
#Buttons to launch or cancel ssh command
def yes ():
    name_get()
    IP_get()
    port_get()
    key_get()
    term_get()
    master.destroy()
    mainfunc()
def no ():
    print("Exiting without launching...")
    master.destroy()
launch = tki.Button(master,text="Launch ssh",command=yes)
launch.grid(row=3,column=1)
cancel = tki.Button(master,text="Cancel",command=no)
cancel.grid(row=3, column=4)
#Run everything with the below:
master.mainloop()
