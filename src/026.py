# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：利用递归方法求 5!。
"""


def solution1(n):
    return n * solution1(n - 1) if n > 1 else 1


def main():
    print('---------- solution 1 ---------- ')
    print('5!：', solution1(5))


if __name__ == '__main__':
    main()
