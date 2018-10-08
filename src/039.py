# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：将一个数组逆序输出。
"""


SORTED_LIST = [1, 5, 9, 10, 22, 45]


def solution1():
    return SORTED_LIST[::-1]


def main():
    print('---------- solution 1 ---------- ')
    print(solution1())


if __name__ == '__main__':
    main()
