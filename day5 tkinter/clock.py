import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.geometry("1200x900")
root.title("Clock")

icon = PhotoImage(file="clock-icon.png")
root.iconphoto(True, icon)

label1 = tk.Label(root, text="Stay on track with focus sessions",  font=("Helvetica", 20, "bold"))
label1.pack(pady=(150, 0))

label2 = tk.Label(root, text="We'll turn off notifications and app alerts during each session. For longer sessions, we'll add a short break so you can recharge.",  font=("Helvetica", 13 ), wraplength=550)
label2.pack()

illustration = PhotoImage(file="clock-illustration.png")
label3 = tk.Label(root, image=illustration)
label3.pack(pady=20)

button = tk.Button(root, text="Get Started", bg="#d197e0", fg="black", padx=65, pady=8, border=0, font=("Helvetica", 12, "bold"))
button.pack()

root.mainloop()