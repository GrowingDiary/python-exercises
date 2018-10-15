# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：学习使用按位与 & 。
"""


def main():
    a = 0xFF
    b = 0x12
    print('a & b =', a & b)
    a &= 0x12
    print('a & 0x12 =', a)


if __name__ == '__main__':
    main()
