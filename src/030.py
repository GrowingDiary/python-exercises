# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""


def solution1(n):
    num_str = str(n)
    return num_str[:len(num_str) // 2] == num_str[-1:(len(num_str) - 1) // 2:-1]


def main():
    input_str = input('输入一个数字：')
    try:
        num = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    print(solution1(num))


if __name__ == '__main__':
    main()
