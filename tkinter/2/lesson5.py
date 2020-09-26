from tkinter import *

root = Tk()
root.geometry('600x400+500+300')

def add_str():
    e.insert(END, ' other Test text')

def del_str():
    e.delete(0, END)

def get_str():
    label1['text'] = e.get()

label = Label(root, text="Entry field")
label.pack()

e = Entry(root)
# e.insert(0, 'Test text')
# e.insert(END, ' other Test text')
e.pack()

btn_add = Button(root, text="Add", command=add_str).pack()
btn_del = Button(root, text="Delete", command=del_str).pack()
btn_get = Button(root, text="Get", command=get_str).pack()

label1 = Label(root, bg="blue")
label1.pack(fill=X)

root.mainloop()