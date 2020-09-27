from tkinter import *

root = Tk()
root.geometry('800x600+1000+300')

frame_menu = Frame(root, bg="#1f252a", height=40)
frame_text = Frame(root)
frame_menu.pack(fill=X)
frame_text.pack(fill=BOTH, expand=1)

label_menu = Label(frame_menu, text="Menu", bg="#2b3239", fg="#c6dec1", font="Arial 10")
label_menu.place(x=10, y=10)

text = Text(frame_text, bg="#343d46", fg="#c6dec1", padx=10, pady=10, 
            wrap=WORD, insertbackground="#eda756", selectbackground="#4e5a65", spacing3=10)
text.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text.yview)
scroll.pack(fill=Y, side=LEFT)
text.config(yscrollcommand=scroll.set)

root.mainloop()