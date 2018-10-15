# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：取一个整数a从右端开始的4〜7位。
"""


def main():
    a = 0x28
    print('a 的右端开始的 4 ~ 7 位：', a >> 4 & 0xF)


if __name__ == '__main__':
    main()
