# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输出 9 * 9 乘法口诀表。
"""


def solution1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{j} x {i} = {k}'.format(i=i, j=j, k=i * j), end=', ')
        print('')


def solution2():
    line_list = []
    for i in range(1, 10):
        line_list.append(', '.join(['{j} x {i} = {k}'.format(i=i, j=j, k=i * j) for j in range(1, i + 1)]))
    print('\n'.join(line_list))


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()


if __name__ == '__main__':
    main()
