import tkinter as tk
from tkinter import PhotoImage

#create the main window
root = tk.Tk()
#see the title of the window
root.title("My tkinter App")

#lead an image file to use as the icon
icon=PhotoImage(file='flo.png')

#set the icon for type window
root.iconphoto(True,icon)

#set the window size
root.geometry("400x200")

#
root.mainloop()