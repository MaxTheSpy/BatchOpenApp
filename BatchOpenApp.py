#Program Adapted from various sources.
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
#Start--------------------------------------------------------------------------
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title = "select file",
    filetypes=(("executables","*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=400, width=700, bg="#e3ae8f")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.01, rely=0.01)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApp = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
openFile.pack()
runApp.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
