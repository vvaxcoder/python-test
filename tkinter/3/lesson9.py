from tkinter import *

root = Tk()
root.geometry('600x400+800+300')

# f_top = Frame(root)
# f_bottom = Frame(root)
# f_top.pack()
# f_bottom.pack()

# f_top = LabelFrame(root, text="Top Frame", padx=10, pady=10)
# f_bottom = LabelFrame(root, text="Bootom Frame", padx=10, pady=10)
# f_top.pack()
# f_bottom.pack()

# label1 = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=TOP)
# label2 = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# label3 = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=RIGHT)
# label4 = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=BOTTOM)

# label1 = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
# label2 = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# label3 = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
# label4 = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

label5 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, fill=Y)

root.mainloop()