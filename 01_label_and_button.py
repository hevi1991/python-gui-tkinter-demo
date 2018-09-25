#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

"""
标签和按钮
"""

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
# lab = tk.Label(window, text='some text', bg='green', font=('Arial', 12), width=15, height=2)
lab = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
lab.pack()

on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()
