#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
画布
"""

import tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x200')

c = tk.Canvas(w, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='./static/temp1.png')
image = c.create_image(0, 0, anchor='nw', image=image_file)
c.pack()


def move_up():
    c.move(image, 0, -2)


def move_left():
    c.move(image, -2, 0)


def move_down():
    c.move(image, 0, 2)


def move_right():
    c.move(image, 2, 0)


b1 = tk.Button(w, text='↑', command=move_up).pack()
b2 = tk.Button(w, text='←', command=move_left).pack()
b3 = tk.Button(w, text='↓', command=move_down).pack()
b4 = tk.Button(w, text='→', command=move_right).pack()

w.mainloop()
