# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵。
"""


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]


def solution1():
    Z = []
    for i in range(len(X)):
        Zi = []
        for j in range(len(X[i])):
            Zi.append(X[i][j] + Y[i][j])
        Z.append(Zi)
    print(Z)


def solution2():
    import itertools
    print(list(
        list(map(sum, j))
        for j in (itertools.zip_longest(i[0], i[1])
                  for i in itertools.zip_longest(X, Y))))


def solution3():
    import numpy
    x = numpy.array(X)
    y = numpy.array(Y)
    print(x + y)


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()
    print('---------- solution 3 ---------- ')
    solution3()


if __name__ == '__main__':
    main()
