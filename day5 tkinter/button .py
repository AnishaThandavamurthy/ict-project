#button to pack layout
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")
def on_submit():
    label1.config(text="reg complete!!!!")
def on_follow():
    label2.config(text="account followed")

root=tk.Tk()
root.title("simple GUI")
root.geometry("300x200")

label=tk.Label(root, text="hello, Tkinter")
label.pack(pady=20)
 
button=tk.Button(root, text="click me", command=on_button_click,bg="red")
button.pack(pady=20)

label1=tk.Label(root,text="submit reg form")
label1.pack(pady=20)

button=tk.Button(root, text="submit", command=on_submit ,bg="blue")
button.pack(pady=20)

label2=tk.Label(root,text='follow for more updates')
label2.pack(pady=20)

button=tk.Button(root, text="follow", command=on_follow , bg="violet")
button.pack(pady=20)
root.mainloop()