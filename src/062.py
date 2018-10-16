# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：画椭圆。
"""
import tkinter


def main():
    canvas = tkinter.Canvas(width=320, height=320, bg='yellow')
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    canvas.create_oval(20, 50, 300, 250)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
