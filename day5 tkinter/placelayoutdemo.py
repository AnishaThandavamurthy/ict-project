import tkinter as tk

root=tk.Tk()
root.title('Testing place layout')
root.geometry('500x200')

label1=tk.Label(root,text='label1',bg='red')
label1.place(x=80,y=50)

label2=tk.Label(root,text='label2',bg='blue')
label2.place(x=150,y=250)

label3=tk.Label(root,text='label3',bg='green')
label3.place(x=250,y=3000)

label4=tk.Label(root,text='label4',bg='violet')
label4.place(x=1500,y=2500)

label5=tk.Label(root,text='label5',bg='brown')
label5.place(x=450,y=350)

root.mainloop()