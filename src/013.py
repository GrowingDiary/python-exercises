# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：打印出所有的水仙花数。

所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个水仙花数，因为 153 = 1 ** 3 ＋ 5 ** 3 ＋ 3 ** 3。

a * 100 + b * 10 + c = a ** 3 + b ** 3 + c ** 3
"""


def solution1():
    narcissistic_number = []
    for i in range(100, 1000):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])

        if i == a ** 3 + b ** 3 + c ** 3:
            narcissistic_number.append(i)
    return narcissistic_number


def solution2():
    return list(filter(lambda x: x == sum([int(i) ** 3 for i in str(x)]), range(100, 1000)))


def main():
    print('---------- solution 1 ---------- ')
    print('水仙花数为：', solution1())
    print('---------- solution 2 ---------- ')
    print('水仙花数为：', solution2())


if __name__ == '__main__':
    main()
