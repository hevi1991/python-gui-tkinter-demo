#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
新窗体
"""

import tkinter as tk

window = tk.Tk()
window.title('main window')
window.geometry('300x200')


def open_new_window():
    top_window = tk.Toplevel(window)
    top_window.title('a new window')
    top_window.geometry('200x100')
    tk.Button(top_window, text='destroy', command=lambda: top_window.destroy()).pack()


tk.Button(window, text='open new window', command=open_new_window).pack()

window.mainloop()
