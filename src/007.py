# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：将一个列表的数据复制到另一个列表中。
"""


def solution1(list_value):
    import copy
    return copy.deepcopy(list_value)


def solution2(list_value):
    return list_value[:]


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = solution1(list1)
    print('---------- solution 1 ---------- ')
    print('list1 == list2:', list1 is list2)
    list3 = solution2(list1)
    print('---------- solution 2 ---------- ')
    print('list1 == list3:', list1 is list3)


if __name__ == '__main__':
    main()
