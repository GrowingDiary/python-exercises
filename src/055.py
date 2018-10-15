# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：画图，学用 circle 画圆形。
"""
import tkinter


def main():
    canvas = tkinter.Canvas(width=320, height=320, bg='yellow')
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    canvas.create_oval(20, 20, 300, 300, width=1)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
