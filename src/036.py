# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：求 100 之内的素数。
"""


def solution1():
    prime_numbers = [2]
    for i in range(2, 100):
        if i % 2 == 0:
            continue
        factor_count = 1
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                factor_count += 1
                break
        if factor_count == 1:
            prime_numbers.append(i)
    print(prime_numbers)


def main():
    print('---------- solution 1 ---------- ')
    solution1()


if __name__ == '__main__':
    main()
