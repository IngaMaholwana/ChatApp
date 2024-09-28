import threading
import tkinter as tk 
from tkinter import ttk 
from ttkthemes import ThemedTk
import client

def send_message():
    pass

#the main window in widgtes 
root = ThemedTk(theme="arc")
root.title("Inga Chat")
root.geometry("400x500")

#makes the widget window resizable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_columnconfigure(0,weight=1)

list_box = tk.Listbox(root) #to display messages
scroll_bar = ttk.Scrollbar(root)
entry = ttk.Entry(root)#to enter text
send_btn = ttk.Button(root, text="Send", command=send_message)


list_box.grid(row=0, column=0, sticky="nsew")
scroll_bar(row=0, column=1, sticky="ns")
entry.grid(row=1, column=0, sticky="ew")
send_btn.grid(row=2, column=0, sticky="ew")

#attach the scroll bar to list box so it scrolls thru the list 
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)