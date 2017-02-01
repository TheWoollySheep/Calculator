from tkinter import *

root = Tk()

def printName(event):
    print("hello my name is kayode")

button_1 = Button(root, text="print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()
# or button_1 = Button(root, text="print my name", command=printName

root.mainloop()
