# Python tkinter hello world program

import tkinter as tk

print("CoNsOlE!")

window = tk.Tk()

lbl_Hello = tk.Label(window, text="Hello World!")
lbl_Hello.grid(row=0, column=0)

lbl_New = tk.Label(window, text="New!")
lbl_New.grid(row=0, column=1)

window.mainloop()

