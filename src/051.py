# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：学习使用按位或 | 。
"""


def main():
    a = 0x10
    b = 0x2
    print('a | b =', a | b)
    a |= 0x2
    print('a | 0x2 =', a)


if __name__ == '__main__':
    main()
