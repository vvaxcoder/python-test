from tkinter import *

root = Tk()
root.geometry('200x200+800+300')

class MyButtons:
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(root, bg=k, command=self.change_color)
        self.button.pack(fill=X)

    def change_color(self):
        label['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

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
    MyButtons(root, v, k)

root.mainloop()