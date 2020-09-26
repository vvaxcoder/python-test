from tkinter import *

root = Tk()
# root.geometry('600x400+800+300')

# frame = Frame(root)
# frame.pack(pady=10)

# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0',
# ]

# row = 0
# column = 0

# for btn in btn_list:
#     if btn == '0':
#         Button(frame, text=btn, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(frame, text=btn, padx=10, pady=5).grid(row=row, column=column)

#     column += 1
#     if column == 3:
#         column = 0
#         row += 1

# btn7 = Button(frame, text="7", padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(frame, text="8", padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(frame, text="9", padx=10, pady=5).grid(row=0, column=2)
# btn4 = Button(frame, text="4", padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(frame, text="5", padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(frame, text="6", padx=10, pady=5).grid(row=1, column=2)
# btn1 = Button(frame, text="1", padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(frame, text="2", padx=10, pady=5).grid(row=2, column=1)
# btn3 = Button(frame, text="3", padx=10, pady=5).grid(row=2, column=2)
# btn0 = Button(frame, text="0", padx=10, pady=5).grid(row=3, column=0, columnspan=3)

label_user = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

label_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
entry_pass = Entry(root, show="*").grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text="Enter", padx=5).grid(row=2, column=0, pady=10)
btn_reg = Button(root, text="Registration", padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text="Forgot password", padx=5).grid(row=2, column=2, padx=10)

root.mainloop()