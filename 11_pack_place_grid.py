#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
布局
"""

import tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x200')


# pack
# tk.Label(w, text='North').pack(side='top')
# tk.Label(w, text='South').pack(side='bottom')
# tk.Label(w, text='West').pack(side='left')
# tk.Label(w, text='East').pack(side='right')

# place 绝对定位
tk.Label(w, text='lorem').place(x=10, y=100, anchor='nw')

# grid
# for i in range(4):
#     for j in range(3):
#         tk.Label(w, text='lorem').grid(row=i, column=j, padx=10, pady=10)

# 运行循环
w.mainloop()