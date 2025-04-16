import tkinter as tk
from tkinter import ttk

def button_clicked():
    print(string_var.get())
    string_var.set("Button clicked!")

#window
window = tk.Tk()
window.title("Learn Tkinter")

#tkinter variables
string_var = tk.StringVar()

label = tk.Label(master = window, text="Label", textvariable=string_var)
label.pack()

entry = tk.Entry(master = window, textvariable=string_var)
entry.pack()

button = ttk.Button(master = window, text="Button", command=button_clicked)
button.pack()

#running
window.mainloop()