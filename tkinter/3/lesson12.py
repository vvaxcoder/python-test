from tkinter import *

root = Tk()
root.geometry('800x600+1000+300')

# frame_menu = Frame(root, bg="#1f252a", height=40)
# frame_text = Frame(root)
# frame_menu.pack(fill=X)
# frame_text.pack(fill=BOTH, expand=1)

main_menu = Menu(root)
root.config(menu=main_menu)
# main_menu.add_command(label="File")
# main_menu.add_command(label="About")

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_cascade(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu.add_command(label="Online")
help_menu.add_command(label="Offline")
main_menu.add_cascade(label="Help", menu=help_menu_sub)
help_menu.add_command(label="About programm")
main_menu.add_cascade(label="Info", menu=help_menu)

# label_menu = Label(frame_menu, text="Menu", bg="#2b3239", fg="#c6dec1", font="Arial 10")
# label_menu.place(x=10, y=10)

# text = Text(frame_text, bg="#343d46", fg="#c6dec1", padx=10, pady=10, 
#             wrap=WORD, insertbackground="#eda756", selectbackground="#4e5a65", spacing3=10)
# text.pack(fill=BOTH, expand=1, side=LEFT)

# scroll = Scrollbar(frame_text, command=text.yview)
# scroll.pack(fill=Y, side=LEFT)
# text.config(yscrollcommand=scroll.set)

root.mainloop()