from tkinter import *

root = Tk()
root.geometry('600x400+500+300')
label = Label(root, text="Text in the line1\nAnother line2\nYep, and new line3 again\nLine4\nLine5", bg="cyan",
             fg="blue", font=("Comic Sans MS", 14, "bold"), justify=LEFT, width=46, anchor=W)
label.pack()

root.mainloop()