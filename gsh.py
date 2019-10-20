import tkinter as tki
import subprocess
#variable creation
name = ''
ip = ''
port = ''
key = ''
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
dest = tki.Label(master, text="Destination IP:")
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
def mainfunc ():
    if key != '' and port != '':
		    sshcom = "ssh " + name + "@" + ip + " -p " + port + " -i " + key
		    process = subprocess.run(sshcom.split())
    if key != '' and port == '':
		    sshcom = "ssh " + name + "@" + ip + " -i " + key
		    process = subprocess.run(sshcom.split())
    if port != '' and key == '':
		    sshcom = "ssh " + name + "@" + ip + " -p " + port
		    process = subprocess.run(sshcom.split())
    if port == '' and key == '':
		    sshcom = "ssh " + name + "@" + ip
		    process = subprocess.run(sshcom.split())
#Buttons to launch or cancel ssh command
def yes ():
    print("Launching ssh...")
    name_get()
    IP_get()
    port_get()
    key_get()
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
