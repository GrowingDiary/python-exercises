# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：画图，学用 line 画直线。
"""
import tkinter


def main():
    canvas = tkinter.Canvas(width=320, height=320, bg='yellow')
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    canvas.create_line(0, 0, 320, 320)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
