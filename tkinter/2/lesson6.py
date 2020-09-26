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

colors = {
    '#ff0000': 'Red',
    '#ff7d00': 'Orange',
    '#ffff00': 'Yellow',
    '#00ff00': 'Green',
    '#007dff': 'Blue',
    '#0000ff': 'Blue',
    '#7d00ff': 'Violet',
}

for k,v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: change_color(text, hex)).pack(fill=X)

root.mainloop()