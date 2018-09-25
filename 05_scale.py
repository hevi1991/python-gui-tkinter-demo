#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
尺度
"""

import tkinter as tk

w = tk.Tk()
w.title = 'my window'

l = tk.Label(w, bg='yellow', width=20, text='empty')
l.pack()


def print_selection(e):
    l.config(text = 'you have selected {0}'.format(e))


s = tk.Scale(w, label='try me', from_=4, to=12, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=4,
             resolution=0.01, command=print_selection)
s.pack()

w.mainloop()
