import tkinter as tk
from tkinter import ttk

nome_usuario = "vinicius"

window = tk.Tk()
window.title("Learn Tkinter")
window.geometry("600x400")

def button_function(nome):
    print(f"hello {nome}")

button = ttk.Button(master = window, text="Click Me!", command=lambda: button_function(nome_usuario))
button.pack()

window.mainloop()