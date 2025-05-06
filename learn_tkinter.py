import tkinter as tk
from tkinter import ttk

nome_usuario = "vinicius"

window = tk.Tk()
window.title("Learn Tkinter")
window.geometry("600x400")

check_var = tk.BooleanVar()
check_radio_var = tk.BooleanVar()

def button_function(nome):
    if check_var.get() and check_radio_var.get() == True:
        print(f"hello {nome} - check is checked")
    else:
        print(f"hello {nome} - check is not checked")

button = ttk.Button(master = window, text="Click Me!", command=lambda: button_function(nome_usuario))
button.pack()

#check button
check = ttk.Checkbutton(window, text="Check me!", variable=check_var)
check.pack()

#radio button
radio_var1 = ttk.Radiobutton(window, text="radio button 1", value=1)
radio_var1.pack()
radio_var2 = ttk.Radiobutton(window, text="radio button 2", value=1, variable=check_radio_var)
radio_var2.pack()
radio_var3 = ttk.Radiobutton(window, text="radio button 3", value=3)
radio_var3.pack()
radio_var4 = ttk.Radiobutton(window, text="radio button 4", value=2, variable=check_radio_var)
radio_var4.pack()
radio_var5 = ttk.Radiobutton(window, text="radio button 5", value=5)
radio_var5.pack()

window.mainloop()