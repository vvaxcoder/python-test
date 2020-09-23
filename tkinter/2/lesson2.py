# https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Second lesson')
root.geometry('600x400+500+300')

def clicked():
    print('Clicked')

# btn = Button(root, text='Button', command=clicked, width=10) # not pixels, znakomesta
# btn = Button(root, text='Button', command=clicked, font='Arial 20 italic')
# btn = Button(root, text='Button', command=clicked, font=('Comic Sans MS', 20, 'italic'))
btn = Button(root, text='Button')
btn.configure(width=20, height=6)
btn['font'] = 'Arial 15'
btn.pack()

# btn2 = ttk.Button(root, text='Button') # button with native OS
# btn2.pack()

root.mainloop()