import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Label, Style
import config_db

if __name__ == '__main__':
    data = [config_db.result]
    window = Tk()
    window.geometry('1200x600')

    frame_top = Frame(window)
    frame_top.pack(side=tkinter.TOP, padx=5)

    frame_left = Frame(window)
    frame_left.pack(side=tkinter.LEFT, padx=20)

    frame_right = Frame(window)
    frame_right.pack(side=tkinter.RIGHT, padx=20)

    tv = ttk.Treeview(frame_left, columns=(1, 2, 3, 4, 5), show='headings', height=15)
    tv.pack()

    tv.heading(1, text='ID')
    tv.heading(2, text='Name')
    tv.heading(3, text='Lastname')
    tv.heading(4, text='Mail')
    tv.heading(5, text='Address')

    lbl1 = tkinter.Label(frame_top, text='Contact book', font=20)
    lbl1.pack()
    for i in config_db.result:
        tv.insert('', 'end', values=i)

    window.title('Contact book')
    window.mainloop()
