import tkinter as tk
from tkinter import ttk

def button_function(entry_string):
    print("Button clicked!")
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print("Inner function called...")
        print(parameter.get())
    return inner_func

window = tk.Tk()
window.title("Learn Tkinter")

#widgets
entry_string = tk.StringVar(value = 'Test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="Click Me", command=outer_func(entry_string))
button.pack()

window.geometry("400x300")
window.mainloop()