import tkinter as tk
from tkinter import filedialog, messagebox

# Create the root window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Create a Text widget for the notepad
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)

# File functions
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("New File - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")

def exit_app():
    root.quit()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",command=new_file )
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

#create the  edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=file_menu)
edit_menu.add_command(label="cut" )
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=file_menu)
view_menu.add_command(label="Zoom" )
view_menu.add_command(label="Status bar")
view_menu.add_command(label="word wrap")

# Run the application
root.mainloop()
