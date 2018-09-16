# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

x ** 2 = z + 100
y ** 2 = z + 100 + 168

y ** 2 - x ** 2 = 168

(y - x) * (y + x) = 168

a * b = 168
y - x = a
y + x = b
y = (a + b) / 2
x = (b - a) / 2
"""


def factor(number):
    step = 2 if number % 2 == 1 else 1
    return filter(lambda x: x is not None,
                  map(lambda i: (i, number // i) if number % i == 0 else None, range(1, int(number ** 0.5) + 1, step)))


def solution1():
    result = [((b - a) // 2, (a + b) // 2) for a, b in factor(168) if (a + b) % 2 == 0]
    return result


def main():
    for x, y in solution1():
        print('----------------------')
        assert(x ** 2 - 100 == y ** 2 - 268)
        print('x = ', x)
        print('y = ', y)
        print('z = ', x ** 2 - 100)
        print('{x} ** 2 = {z} + 100'.format(x=x, z=x * x - 100))
        print('{y} ** 2 = {z} + 268'.format(y=y, z=y * y - 268))


if __name__ == '__main__':
    main()
