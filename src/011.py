# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

月份：1    2   3   4   5   6   7   8
数量：1    1   2   3   5   8   13  21
斐波那契数列
"""


def solution1(length):
    fibonacci_seq = []
    for i in range(length):
        if i < 2:
            fibonacci_seq.append(1)
            continue
        fibonacci_seq.append(sum(fibonacci_seq[-2:]))
    return fibonacci_seq


def main():
    input_str = input('输入月数：')
    try:
        month_count = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    print('兔子总数为：', solution1(month_count)[-1])


if __name__ == '__main__':
    main()
