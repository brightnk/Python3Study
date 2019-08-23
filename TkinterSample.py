from tkinter import *
import tkinter.messagebox as messageBox

class MyButtons:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="delete line", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack()

    def printmessage(self):
        print("Button Clicked")
        canvas.delete(line)


def menutest():
    print("Menu test clicked")

def fileinsert():
    messageBox.showinfo("title", "this is going to insert file")
    response = messageBox.askquestion("questions", "do you want to insert file")
    if response:
        print("going to insert file")
    else:
        print("insert file is abort")

def deleteline():
    canvas.delete(line)

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
mymenu.add_command(label="test", command=menutest)
submenu.add_command(label="Project", command=menutest)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

toolbar = Frame(root, bg="pink")
insertbutton = Button(toolbar, text="Insert Files", command=fileinsert)
insertbutton.pack(side=LEFT, padx=2,pady=3)
printbutton = Button(toolbar, text="deleteline", command=deleteline)
printbutton.pack(side=LEFT, padx=2,pady=3)
toolbar.pack(side=TOP, fill=X)

canvas = Canvas(root, width=200, height=100)
canvas.pack()
line = canvas.create_line(0, 0, 50, 100)
canvas.create_line(10, 10, 100, 100, fill="green")




b = MyButtons(root)
statusbar = Label(root, text="this is the status", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
