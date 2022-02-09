from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Catch Phrase V1.1")

mainframe = ttk.Frame(root, padding="6 6 16 16")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


root.mainloop()