# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
     第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
     以后每天早上都吃了前一天剩下的一半零一个。
     到第 10 天早上想再吃时，见只剩下一个桃子了。
     求第一天共摘了多少？
"""


def solution1():
    n = 1
    for i in range(9):
        n = (n + 1) * 2
    return n


def solution2(n):
    return 1 if n == 1 else (solution2(n - 1) + 1) * 2


def main():
    print('---------- solution 1 ---------- ')
    print('第一天摘了', solution1(), '个桃子')
    print('---------- solution 2 ---------- ')
    print('第一天摘了', solution2(10), '个桃子')


if __name__ == '__main__':
    main()
