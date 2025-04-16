import tkinter as tk
from tkinter import ttk
import time

def button_function():
    # Obtem o texto do entry e coloca na label
    label["text"] = entry.get()
    print(entry.get())

    entry['state'] = 'disabled'  # Desabilita o campo de texto

    # Limpa o campo de texto
    entry.delete(0, tk.END)
    time.sleep(5)  # Espera 5 segundos
    entry['state'] = 'normal'  # Habilita o campo de texto
    # Coloca o foco no campo de texto

window = tk.Tk()
window.title("Aprendendo Tkinter")

#widgets: elementos da interface
#label: texto
label = ttk.Label(master = window, text="um texto")
label.pack()

#entry: campo de texto
entry = ttk.Entry(master = window)
entry.pack()

#button: botão
button = ttk.Button(master = window, text="Clique aqui!", command=button_function)
button.pack()

#mainloop mantem a janela aberta
window.mainloop()