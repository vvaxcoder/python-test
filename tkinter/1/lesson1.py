# https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *

root = Tk()
root.title('This is my GUI title')
# root.iconbitmap('test.ico') #not working
root.geometry('600x400+500+300')
root.resizable(True, False)
root.config(bg='yellow')

root.mainloop()