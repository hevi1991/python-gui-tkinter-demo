#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多选按钮
"""

import tkinter as tk

w = tk.Tk()
w.title = 'my window'

l = tk.Label(w, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if var1.get() == 1 and var2.get() == 1:
        l.config(text='I love both')
    elif var1.get() == 1:
        l.config(text='I love only Python')
    elif var2.get() == 1:
        l.config(text='I love only C++')
    else:
        l.config(text='I do not love neither')


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(w, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(w, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

w.mainloop()
