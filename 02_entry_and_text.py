#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

"""
输入和文本框
"""

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# e = tk.Entry(window, show='*')
e = tk.Entry(window)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
