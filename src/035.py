# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：文本颜色设置。
"""


def solution1():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[5;93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)


def solution2():
    fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

    def print_six(row, f):
        for col in range(6):
            color = row * 6 + col + 4
            if color >= 0:
                text = "{:3d}".format(color)
                print(f(text, color), end=" ")
            else:
                print("   ", end=" ")

    for r in range(-1, 42):
        print_six(r, fg)
        print("", end=" ")
        print_six(r, bg)
        print()


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()


if __name__ == '__main__':
    main()
