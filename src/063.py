# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输入 3 个数 a, b, c，按大小顺序输出。
"""
import random


def solution1(*num):
    num_list = list(num)
    num_list.sort()
    print(num_list)


def main():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)

    print('---------- solution 1 ---------- ')
    solution1(a, b, c)


if __name__ == '__main__':
    main()
