from tkinter import *
import time

root = Tk()
root.title('Counter')
root.geometry('600x400+500+300')

def check_time():
    # print(time.strftime('%H:%M:%S'))
    btn_time['text'] = time.strftime('%H:%M:%S')

clicks = 0
def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')

btn_time = Button(root, text='Check time', command=check_time)
btn_time.pack()

btn_cnt = Button(root, text='Counter', command=counter)
btn_cnt.pack()

root.mainloop()