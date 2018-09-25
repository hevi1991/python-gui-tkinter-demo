#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
单选按钮
"""

import tkinter as tk

w = tk.Tk()
w.title = 'my window'

l = tk.Label(w, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.StringVar()


def print_selection():
    l.config(text='you have selected {0}'.format(var1.get()))


r1 = tk.Radiobutton(w, text='Option A', variable=var1, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(w, text='Option B', variable=var1, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(w, text='Option C', variable=var1, value='C', command=print_selection)
r3.pack()

# Radiobutton中的variable用于判定单选按钮是否唯一

l2 = tk.Label(w, bg='yellow', width=20, text='empty')
l2.pack()

var2 = tk.StringVar()

def print_selection_2():
    l2.config(text='you have selected {0}'.format(var2.get()))


r4 = tk.Radiobutton(w, text='Option A', variable=var2, value='D', command=print_selection_2)
r4.pack()
r5 = tk.Radiobutton(w, text='Option B', variable=var2, value='E', command=print_selection_2)
r5.pack()
r6 = tk.Radiobutton(w, text='Option C', variable=var2, value='F', command=print_selection_2)
r6.pack()


w.mainloop()
