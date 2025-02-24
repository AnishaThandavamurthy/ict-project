import tkinter as tk


root = tk.Tk()
root.title("Calculator")


input_field = tk.Entry(root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_1 = tk.Button(root, text="1", padx=40, pady=20)
button_2 = tk.Button(root, text="2", padx=40, pady=20)
button_3 = tk.Button(root, text="3", padx=40, pady=20)
button_4 = tk.Button(root, text="4", padx=40, pady=20)
button_5 = tk.Button(root, text="5", padx=40, pady=20)
button_6 = tk.Button(root, text="6", padx=40, pady=20)
button_7 = tk.Button(root, text="7", padx=40, pady=20)
button_8 = tk.Button(root, text="8", padx=40, pady=20)
button_9 = tk.Button(root, text="9", padx=40, pady=20)
button_0 = tk.Button(root, text="0", padx=40, pady=20)

button_add = tk.Button(root, text="+", padx=39, pady=20)
button_subtract = tk.Button(root, text="-", padx=41, pady=20)
button_multiply = tk.Button(root, text="*", padx=40, pady=20)
button_divide = tk.Button(root, text="/", padx=41, pady=20)

button_equal = tk.Button(root, text="=", padx=87, pady=20)
button_clear = tk.Button(root, text="Clear", padx=77, pady=20)
button_delete = tk.Button(root, text="Delete", padx=30, pady=20)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)

button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=4, column=3, columnspan=2)
button_delete.grid(row=1, column=3)

root.mainloop()
