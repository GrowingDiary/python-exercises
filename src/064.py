# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""
import copy
import random


def solution1(num):
    print(num)
    max_pos = 0
    min_pos = 0
    for i in range(len(num)):
        if num[i] < num[min_pos]:
            min_pos = i
        if num[i] > num[max_pos]:
            max_pos = i

    num[0], num[max_pos] = num[max_pos], num[0]
    num[-1], num[min_pos] = num[min_pos], num[-1]
    print(num)


def solution2(num):
    print(num)
    max_pos = num.index(max(num))
    min_pos = num.index(min(num))
    num[0], num[max_pos] = num[max_pos], num[0]
    num[-1], num[min_pos] = num[min_pos], num[-1]
    print(num)


def main():
    num_list = []
    for i in range(10):
        num_list.append(random.randint(0, 100))

    print('---------- solution 1 ---------- ')
    solution1(copy.deepcopy(num_list))
    print('---------- solution 2 ---------- ')
    solution2(copy.deepcopy(num_list))


if __name__ == '__main__':
    main()
