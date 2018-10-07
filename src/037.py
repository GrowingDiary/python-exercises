# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：求一个 3 * 3 矩阵主对角线元素之和。
"""


def solution1(*l):
    return l[0][0] + l[1][1] + l[2][2]


def solution2(*l):
    return sum([l[i][i] for i in range(len(l))])


def main():
    print('---------- solution 1 ---------- ')
    print(solution1([1, 2, 3], [1, 2, 3], [1, 2, 3]))
    print('---------- solution 2 ---------- ')
    print(solution2([1, 2, 3], [1, 2, 3], [1, 2, 3]))


if __name__ == '__main__':
    main()
