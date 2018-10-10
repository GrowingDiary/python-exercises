# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：统计 1 到 100 之和。
"""


def solution1():
    print(sum(range(1, 101)))


def solution2():
    print((1 + 100) * 100 // 2)


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()


if __name__ == '__main__':
    main()
