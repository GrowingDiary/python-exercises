# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：判断101-200之间有多少个素数，并输出所有素数。

质数（素数）定义为在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数。
"""


def solution1(start, end):
    prime_numbers = []
    for i in range(start, end):
        if i % 2 == 0:
            continue

        has_factor = False
        for factor in range(3, int(i ** 0.5) + 1, 2):
            if i % factor == 0:
                has_factor = True
                break

        if not has_factor:
            prime_numbers.append(i)
    return prime_numbers


def main():
    start = input('输入开始：')
    end = input('输入结束：')

    try:
        start = int(start)
        end = int(end)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('---------- solution 1 ---------- ')
    print('素数为：', solution1(start, end))


if __name__ == '__main__':
    main()
