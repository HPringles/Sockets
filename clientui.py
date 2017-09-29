from tkinter import *
from tkinter import ttk
import client
import type_test

root = Tk()

# Set the window Title
root.title = ("Chat")

#create a new frame
mainframe = ttk.Frame(root, padding="10")

s = ttk.Style()

# add the grame to the window(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#allow frame to stretch on resize
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

#set_up variables

server_ip = StringVar()
server_port = StringVar()
username = StringVar()
message_list = []

# Add Title, ip,username and port fields/labels

ttk.Label(mainframe, text="Chat App", font=("Arial", 20, "bold")).grid(column=1, row=1, columnspan=4, sticky=(N,E))

ttk.Label(mainframe, text="Server IP", font=("Arial", 11)).grid(column=1,row=2,sticky=(W))
ttk.Entry(mainframe, textvariable=server_ip).grid(column=2, row=2, columnspan=2,sticky=(W))

ttk.Label(mainframe, text= "Server Port", font=("Arial", 11)).grid(column=4, row = 2, sticky=W)
ttk.Entry(mainframe, textvariable=server_port).grid(column=5, row=2, columnspan=2, sticky=W)

ttk.Label(mainframe, text="Username", font=("Arial", 11)).grid(column=1, row = 3, sticky=(W))
ttk.Entry(mainframe, textvariable=username).grid(column=2, row=3,columnspan=2,sticky=(W))

connect_button = ttk.Button(mainframe, text="Connect")
connect_button.config(command=lambda: dispatcher("cn"))
connect_button.grid(column=5, row=3, columnspan=2, sticky=W)


send_button = ttk.Button(mainframe, text="send")
send_button.config(command=lambda: dispatcher("sn"))
send_button.grid(column=1, row=4, sticky=W)





#Dispatcher
connection_list = []


def dispatcher(event):
    if event == "cn":
        if type_test.is_int(server_port.get()):
            connection = client.Main().main_loop(server_ip.get(), int(server_port.get()), username.get())
            connection.send_message("Hello World")


root.mainloop()



