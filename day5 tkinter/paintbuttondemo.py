import tkinter as tk

def on_button_click():
    label.config(text="new file")
def edit_file():
    label1.config(text="Edit file")
def view_file():
    label2.config(text="View file")
def save_file():
    label3.config(text="save file")
def back_file():
    label4.config(text="go back to old file ")

root=tk.Tk()
root.title("Paint")
root.geometry("300x200")

label=tk.Label(root, text="File")
label.grid(row=1,column=0)
 
button=tk.Button(root, text="File", command=on_button_click,bg="red")
button.grid(row=0,column=0)

label1=tk.Label(root,text="edit")
label1.grid(row=2,column=0)

button=tk.Button(root, text="Edit", command=edit_file ,bg="blue")
button.grid(row=0,column=1)

label2=tk.Label(root,text='view')
label2.grid(row=3,column=0)

button=tk.Button(root, text="view", command=view_file, bg="violet")
button.grid(row=0,column=2)

label3=tk.Label(root,text='save')
label3.grid(row=4,column=0)

button=tk.Button(root, text="save", command=save_file, bg="green")
button.grid(row=0,column=3)

label4=tk.Label(root,text='back')
label4.grid(row=5,column=0)

button=tk.Button(root, text="back", command=back_file , bg="yellow")
button.grid(row=0,column=3)


root.mainloop()