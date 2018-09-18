# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：将一个正整数分解质因数。例如：输入 90，打印出 90 = 2 * 3 * 3 * 5。
"""


def solution1(number):
    def factor(num):
        if num % 2 == 0:
            return 2

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return i

        return num

    factors = []
    while True:
        f = factor(number)
        factors.append(str(f))
        if f == number:
            break
        number = number // f

    return factors


def solution2(number):
    def factor(num):
        if num > 2 and num % 2 == 0:
            return '2 * ' + factor(num // 2)

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return str(i) + ' * ' + factor(num // i)

        return str(num)

    return factor(number)


def main():
    input_str = input('输入一个正整数：')
    number = 0
    try:
        number = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('---------- solution 1 ---------- ')
    print(number, '=', ' * '.join(solution1(number)))
    print('---------- solution 2 ---------- ')
    print(number, '=', solution2(number))


if __name__ == '__main__':
    main()
