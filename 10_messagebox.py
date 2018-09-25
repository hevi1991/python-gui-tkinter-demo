#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
弹窗
"""

import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
w.title('my window')
w.geometry('200x200')


def hit_me():
    # 提示
    # tk.messagebox.showinfo(title='Hi', message='World!')
    # 警告
    # tk.messagebox.showwarning(title='warning', message='OMG!')
    # 报错
    # tk.messagebox.showerror(title='error', message='Quit')

    # 询问, 返回yes或no的字符串
    # rest = tk.messagebox.askquestion(title='Asking', message='confirm do something.')
    # 询问, 返回True或False的字符串
    rest = tk.messagebox.askyesno(title='Asking', message='confirm do something.')
    print(rest)

tk.Button(w, text='hit me', command=hit_me).pack()

w.mainloop()
