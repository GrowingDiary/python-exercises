# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：两个变量值互换。
"""


def main():
    a = 1
    b = 2
    print('a:', a, 'b:', b)
    a, b = b, a
    print('a:', a, 'b:', b)


if __name__ == '__main__':
    main()
