# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""


def solution1(n):
    num_str = str(n)
    print('位数：', len(num_str))
    print('逆序：', num_str[::-1])


def solution2(n):
    c = 0
    new_num = []
    while n // 10 > 0:
        new_num.append(str(n % 10))
        c += 1
        n //= 10

    if n > 0:
        new_num.append(str(n % 10))
        c += 1
    print('位数：', c)
    print('逆序：', ''.join(new_num))


def main():
    input_str = input('输入一个不多于5位的正整数：')
    try:
        num = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    solution1(num)
    print('---------- solution 2 ---------- ')
    solution2(num)


if __name__ == '__main__':
    main()
