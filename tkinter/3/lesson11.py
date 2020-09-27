from tkinter import *

root = Tk()
root.geometry('600x400+800+300')

# label = Label(root, text="Lesson11", bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
# label.place(x=0, y=0, anchor="w")

# label = Label(root, text="Lesson11", bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
# label.place(relx=0.5, rely=0.5)

label = Label(root, bg="#000")
label.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

root.mainloop()