# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：按逗号分隔列表。
"""


def solution1(l):
    print(','.join(l))


def solution2(l):
    for i in l:
        print(i, end=',')


def main():
    show_list = ['a', 'b', 'c', 'd']
    print('---------- solution 1 ---------- ')
    solution1(show_list)
    print('---------- solution 2 ---------- ')
    solution2(show_list)


if __name__ == '__main__':
    main()
