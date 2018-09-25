#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
布局用, 框架
"""

import tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x200')
tk.Label(w, text='on the window').pack()

frm = tk.Frame(w)
frm.pack()

frm_left = tk.Frame(frm)
frm_left.pack(side='left')

frm_right = tk.Frame(frm)
frm_right.pack(side='right')

tk.Label(frm_left, text='on the frm left 1').pack()
tk.Label(frm_left, text='on the frm left 2').pack()
tk.Label(frm_right, text='on the frm right').pack()

w.mainloop()
