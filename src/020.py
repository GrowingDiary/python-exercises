# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半。求它在第10次落地时，共经过多少米？第10次反弹多高？
"""


def solution1(down_count):
    height_list = [100 / (2 ** i) for i in range(down_count)]
    return height_list[-1], sum(height_list) * 2 - height_list[0]


def main():
    print('---------- solution 1 ---------- ')
    height, total = solution1(10)
    print('最后一次反弹高度：', height / 2)
    print('总共经过：', total)


if __name__ == '__main__':
    main()
