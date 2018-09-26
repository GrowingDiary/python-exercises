# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：求 1 + 2! + 3! + ... + 20! 的和。
"""


def solution1():
    import math

    total = 0
    for i in range(1, 21):
        total += math.factorial(i)

    return total


def solution2():
    import math
    return sum(map(math.factorial, range(1, 21)))


def solution3():
    def factorial(num):
        fac = num
        while num > 1:
            num -= 1
            fac *= num
        return fac

    return sum(map(factorial, range(1, 21)))


def main():
    print('---------- solution 1 ---------- ')
    print('和为：', solution1())
    print('---------- solution 2 ---------- ')
    print('和为：', solution2())
    print('---------- solution 3 ---------- ')
    print('和为：', solution3())


if __name__ == '__main__':
    main()
