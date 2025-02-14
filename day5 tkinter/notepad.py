import tkinter as tk
# from tkinter import filedialog, messagebox


root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)



menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New" )
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")

#create the  edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut" )
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom" )
view_menu.add_command(label="Status bar")
view_menu.add_command(label="word wrap")


root.mainloop()
