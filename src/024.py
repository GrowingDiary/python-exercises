# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13 ... 求出这个数列的前20项之和。
"""


def solution1():
    numerator = 2
    denominator = 1
    total = 0
    for i in range(0, 20):
        total += numerator / denominator
        numerator, denominator = numerator + denominator, numerator
    print('和为：', total)


def solution2():
    def fibonacci(n):
        return int(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (2 ** n * 5 ** 0.5))

    import itertools
    fib_seq = list(map(fibonacci, range(1, 20 + 3)))
    print('和为：', sum([i / j for i, j in itertools.zip_longest(fib_seq[2:], fib_seq[1:-1])]))


def solution3():
    def fibonacci(n):
        return int(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (2 ** n * 5 ** 0.5))

    import itertools
    fib_seq = list(map(fibonacci, range(1, 20 + 3)))
    print('和为：', sum(map(lambda i: i[0] / i[1], itertools.zip_longest(fib_seq[2:], fib_seq[1:-1]))))


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()
    print('---------- solution 3 ---------- ')
    solution3()


if __name__ == '__main__':
    main()
