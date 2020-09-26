from tkinter import *

root = Tk()
root.geometry('200x200+800+300')

def change_color(text_color, hex_color):
    label['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)

label = Label(root)
label.pack()

e = Entry(root, width=30, justify="center")
e.pack()

btn_red = Button(root, bg="red", command=lambda: change_color('Red', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg="orange", command=lambda: change_color('Orange', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg="yellow", command=lambda: change_color('Yellow', '#ffff00')).pack(fill=X)

root.mainloop()