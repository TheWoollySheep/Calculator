from tkinter import *

class KayodesButtons:

    def _init_ (self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", comand=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="quit", comand=frame.quitButton)
        self.quitButton.pack(side=LEFT)

        button1 = Button(master, text="Button 1")

    def printMessage(self):
        print ("Wow, this is AMAZING")

root = Tk()
def act (KayodesButtons):
    act.(self)
root.mainloop()
