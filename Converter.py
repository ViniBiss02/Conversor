import tkinter as tk
from tkinter import ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.60934
    output_string.set(km_output)

window = tk.Tk()
window.title("Simple GUI")
window.geometry("300x200")

title_label = ttk.Label(master = window, text="Miles to Kilometers Converter", font=("Arial", 16))
title_label.pack(pady=10)

input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable = entry_int, width=10)
button = ttk.Button(master=input_frame, text="Convert", command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text = "output", 
                         font=("Arial", 12), 
                         textvariable = output_string)
output_label.pack(pady=10)

window.mainloop()