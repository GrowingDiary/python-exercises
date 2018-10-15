# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：画图，综合例子。
"""
import tkinter


def main():
    canvas = tkinter.Canvas(width=320, height=320, bg='yellow')
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    canvas.create_polygon(160, 20, 20, 160, 160, 300, 300, 160, fill='red')
    canvas.create_rectangle(20, 20, 300, 300)
    canvas.create_oval(20, 20, 300, 300)
    canvas.create_line(20, 20, 300, 300)
    canvas.create_line(20, 300, 300, 20)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
