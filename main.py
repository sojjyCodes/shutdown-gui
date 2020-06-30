import os
import tkinter
import tkinter as tk

root = tkinter.Tk()
root.resizable(height=None, width=None)

label = tk.Label(root, text="My First Tkinter program", bg="black", fg="white")
label.pack()

button_s = tk.Button(text="Shutdown", bg="white", fg="grey", command=os.system("poweroff"))
button_s.pack()

button_r = tk.Button(text="Reboot", bg="white", fg="grey", command=os.system("reboot"))
button_r.pack()

button_quit = tk.Button(text="exit", bg="white", fg="grey", command=exit)
button_quit.pack()

root.mainloop()
