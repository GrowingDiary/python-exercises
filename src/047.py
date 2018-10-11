# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：数字比较。
"""


def main():
    a = 10
    b = 20
    if a < b:
        print(a, '<', b)
    elif a == b:
        print(a, '=', b)
    else:
        print(a, '>', b)

    if 10 < b < 30:
        print(10, '<', b, '<', 30)

    if 1 <= a < 15:
        print(1, '<=', a, '<', 15)


if __name__ == '__main__':
    main()
