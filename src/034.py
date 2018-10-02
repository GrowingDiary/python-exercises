# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：练习函数调用。
"""


def solution1(*l):
    print(l)


def solution2(**kwargs):
    print(kwargs)


def solution3(a, b=1, c=2):
    print(a, b, c)


def solution4(a, *b):
    print(a, b)


def solution5(*b, **c):
    print(b, c)


def main():
    print('---------- solution 1 ---------- ')
    solution1('a', 'b', 'c', 'd')
    print('---------- solution 2 ---------- ')
    solution2(a=1, b=2, c=3, d=4)
    print('---------- solution 3 ---------- ')
    solution3(1)
    solution3(1, 2, 3)
    solution3(1, c=2, b=3)
    solution3(c=2, b=3, a=1)
    print('---------- solution 4 ---------- ')
    solution4(1, 2, 3, 4, 5)
    print('---------- solution 5 ---------- ')
    solution5(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4)


if __name__ == '__main__':
    main()
