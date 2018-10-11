# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：使用 lambda 来创建匿名函数。
"""


def main():
    # do not assign a lambda expression, use a def
    a = lambda x, y: x + y
    print(a(10, 20))


if __name__ == '__main__':
    main()
