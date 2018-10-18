# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
"""
import copy
import random


def solution1(num, swap_size):
    print(num)
    for i in range(swap_size):
        num.insert(0, num.pop())
    print(num)


def solution2(num, swap_size):
    print(num)
    swap_num = num[-swap_size:]
    swap_num.extend(num[:-swap_size])
    print(swap_num)


def solution3(num, swap_size):
    import collections

    print(num)
    num_deque = collections.deque(num)
    num_deque.rotate(swap_size)
    print(list(num_deque))


def main():
    num_list = []
    for i in range(10):
        num_list.append(random.randint(0, 100))

    swap_size = random.randint(1, 9)
    print('m:', swap_size)

    print('---------- solution 1 ---------- ')
    solution1(copy.deepcopy(num_list), swap_size)
    print('---------- solution 2 ---------- ')
    solution2(copy.deepcopy(num_list), swap_size)
    print('---------- solution 3 ---------- ')
    solution3(copy.deepcopy(num_list), swap_size)


if __name__ == '__main__':
    main()
