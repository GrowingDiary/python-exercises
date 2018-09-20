# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如 6 = 1 ＋ 2 ＋ 3。编程找出1000以内的所有完数。
"""


def factor(number):
    factors = [1]
    step = 2 if number % 2 == 1 else 1
    for i in map(lambda i: i if number % i == 0 else None, range(1, int(number ** 0.5) + 1, step)):
        if i is None or i == 1:
            continue
        factors.extend([i, number // i])
    return factors


def solution1():
    return [i for i in range(1, 1000) if sum(factor(i)) == i]


def solution2():
    perfect_numbers = []
    for i in range(1, 1000):
        s = 0
        step = 2 if i % 2 == 1 else 1
        for j in range(1, int(i ** 0.5) + 1, step):
            if i % j == 0:
                if j == 1:
                    s += 1
                    continue
                s += (j + i // j)

        if s == i:
            perfect_numbers.append(i)
    return perfect_numbers


def main():
    print('---------- solution 1 ---------- ')
    print('所有完数：', solution1())
    print('---------- solution 2 ---------- ')
    print('所有完数：', solution2())


if __name__ == '__main__':
    main()
