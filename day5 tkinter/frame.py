import tkinter as tk

root=tk.Tk()
root.title("main component example")

frame=tk.Frame(root, bg="lightgrey", bd=2,relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

label=tk.Label(frame,text="This is a label")
label.pack(padx=5,pady=5)

button=tk.Button(frame,text="This is a button")
button.pack(padx=5,pady=5)

root.mainloop()