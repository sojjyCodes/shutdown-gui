import os
import tkinter
import tkinter as tk
import tkinter.messagebox

def shutdown():
  prompt = tkinter.messagebox.askyesno("Warning ", "You are about to shutdown your system. Do you want to proceed? ")
  if prompt == True:
    os.system("poweroff")
  
def restart():
  confirm = tkinter.messagebox.askyesno("Warning ", "You are about to reboot your system. Do you want to proceed? ")
  if comfirm == True:
    os.system("reboot")


root = tkinter.Tk()
root.configure(bg="black")
root.title("Control centre")
root.geometry("250x570")


label = tk.Label(root, text="My First Tkinter program", bg="white", fg="black", width="24", height="2")
label.pack()

label1 = tk.Label(root, bg="black")
label1.pack()

button_s = tk.Button(text="Shutdown", bg="black", fg="white", width="20", height="10", command= shutdown)
button_s.pack()

label2 = tk.Label(root, bg="black")
label2.pack()

button_r = tk.Button(text="Reboot", bg="black", fg="white", width="20", height="10", command= restart)
button_r.pack()

label3 = tk.Label(root, bg="black")
label3.pack()

button_quit = tk.Button(text="exit", bg="black", fg="white",width="20", height="10", command= exit)
button_quit.pack()

root.mainloop()