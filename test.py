# Python tkinter hello world program

import tkinter as tk

print("CoNsOlE!")

window = tk.Tk()

lbl_Hello = tk.Label(window, text="Hello World!")
lbl_Hello.pack()

window.mainloop()

