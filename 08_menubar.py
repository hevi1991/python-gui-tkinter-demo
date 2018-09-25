#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
菜单栏
"""

import tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x200')

counter = 0


def do_job():
    global counter
    l.config(text='do {0}'.format(counter))
    counter += 1


l = tk.Label(w, text='', bg='yellow')
l.pack()

m = tk.Menu(w)
file_menu = tk.Menu(m, tearoff=0)
m.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=do_job)
file_menu.add_command(label='Open', command=do_job)
file_menu.add_command(label='Save', command=do_job)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=w.quit)

sub_menu = tk.Menu(file_menu)
file_menu.add_cascade(label='Import', menu=sub_menu, underline=0)
sub_menu.add_command(label='Submenu1', command=do_job)

edit_menu = tk.Menu(m, tearoff=0)
m.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=do_job)
edit_menu.add_command(label='Copy', command=do_job)
edit_menu.add_command(label='Paste', command=do_job)


w.config(menu=m)
w.mainloop()
