# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：按相反的顺序输出列表的值。
"""


def solution1(l):
    print(l[::-1])


def solution2(l):
    for i in range(len(l) - 1, -1, -1):
        print(l[i], end=' ')


def main():
    show_list = ['a', 'b', 'c', 'd']
    print('---------- solution 1 ---------- ')
    solution1(show_list)
    print('---------- solution 2 ---------- ')
    solution2(show_list)


if __name__ == '__main__':
    main()
