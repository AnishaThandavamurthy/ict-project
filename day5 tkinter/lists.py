import tkinter as tk

root=tk.Tk()
root.title('Example of lists')

listbox=tk.Listbox(root)
listbox.pack()

listbox.insert(1,"item 1")
listbox.insert(2,"item 2")
listbox.insert(3,"item 3")

root.mainloop()