import tkinter as tk

root=tk.Tk()
root.title("grid ayout with Different widget")
root.geometry("300x300")

label=tk.Label(root,text="this is a label", bg="lightblue")
button=tk.Button(root,text="click me")
entry=tk.Entry(root)
text=tk.Text(root, height=5, width=30)
checkbutton=tk.Checkbutton(root, text="click me") 
radiobutton1=tk.Radiobutton(root,text="option 1", value=1)
radiobutton2=tk.Radiobutton(root,text="option 1", value=2)

label.grid(row=0,column=0,padx=10,pady=10,sticky='w')
button.grid(row=0,column=1,padx=10,pady=10,sticky='e')
entry.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky='ew')
text.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky='w')
checkbutton.grid(row=3,column=0,pady=10,sticky='w')
radiobutton1.grid(row=3,column=1,padx=10,pady=10,sticky='e')
radiobutton2.grid(row=4,column=1,padx=10,pady=10,sticky='e')

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()
