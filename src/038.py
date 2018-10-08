# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""


SORTED_LIST = [1, 5, 9, 10, 22, 45]


def solution1(l, n):
    """
    顺序查找
    """
    i = 0
    for i in range(len(l)):
        if l[i] < n:
            continue
        break

    l.append(n) if l[-1] < n else l.insert(i, n)
    return l


def solution2(l, n):
    """
    折半查找
    """
    def insert_pos(start, end):
        if start > end:
            return start

        i = (end + start) // 2
        if l[i] > n:
            return insert_pos(start, i - 1)
        if l[i] < n:
            return insert_pos(i + 1, end)
        return i

    pos = insert_pos(0, len(l) - 1)
    l.append(n) if l[-1] < n else l.insert(pos, n)
    return l


def main():
    input_str = input('输入要插入的值：')
    try:
        insert_num = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    print(SORTED_LIST)
    print(solution1(SORTED_LIST[:], insert_num))
    print('---------- solution 2 ---------- ')
    print(SORTED_LIST)
    print(solution2(SORTED_LIST[:], insert_num))


if __name__ == '__main__':
    main()
