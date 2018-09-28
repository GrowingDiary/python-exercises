# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""


def solution1(n):
    return n[-1] + solution1(n[:-1]) if len(n) > 1 else n


def solution2(n, i):
    print(n[i - 1], end='')
    if i == 1:
        return
    solution2(n, i - 1)


def main():
    input_str = 'abcdef'
    print('---------- solution 1 ---------- ')
    print(solution1(input_str))
    print('---------- solution 2 ---------- ')
    solution2(input_str, len(input_str))


if __name__ == '__main__':
    main()
