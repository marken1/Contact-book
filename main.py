import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Frame, Label, Style
import config_db

if __name__ == '__main__':
    data = [config_db.result]
    window = Tk()
    window.geometry('1200x600')
    window.columnconfigure(0, weight=2)

    frame_top = Frame(window)
    frame_top.pack(side=TOP)

    frame_bottom = Frame(window)
    frame_bottom.pack(side=BOTTOM)


    def test():
        print('Test')


    insert = tkinter.Button(frame_top, text='Insert', command=test, pady=10, padx=15)
    insert.pack()
    select = tkinter.Button(frame_top, text='Select', command=test, pady=10, padx=15)
    select.pack()
    delete = tkinter.Button(frame_top, text='Delete', command=test, pady=10, padx=15)
    delete.pack()

    for i in range(len(config_db.result)-1):  # row
        e1 = tkinter.Label(frame_bottom, width=10, text='id')
        e1.grid(row=0, column=0)
        e2 = tkinter.Label(frame_bottom, width=10, text='Firstname')
        e2.grid(row=0, column=1)
        e3 = tkinter.Label(frame_bottom, width=10, text='Lastname')
        e3.grid(row=0, column=2)
        e4 = tkinter.Label(frame_bottom, width=10, text='Email')
        e4.grid(row=0, column=3)
        e5 = tkinter.Label(frame_bottom, width=10, text='Address')
        e5.grid(row=0, column=4)
        for k in range(5):  # column
            e = Entry(frame_bottom, width=30)
            e.grid(row=i, column=k)
            e.insert(END, config_db.result[i][k])

    frame_top.pack(pady=50, padx=10)
    frame_bottom.pack(pady=100, padx=10)
    window.mainloop()
