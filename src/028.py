# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有 5 个人坐在一起，问第 5 个人多少岁？他说比第 4 个人大 2 岁。
     问第 4 个人岁数，他说比第 3 个人大 2 岁。
     问第 3 个人，又说比第 2 人大 2 岁。
     问第 2 个人，说比第 1 个人大 2 岁。
     最后问第 1 个人，他说是10岁。
     请问第 5 个人多大？
"""


def solution1(n):
    return 10 + (n - 1) * 2


def solution2(n):
    return 2 + solution2(n - 1) if n > 1 else 10


def main():
    input_str = input('求第几个人的年龄：')
    try:
        num = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    print(solution1(num))
    print('---------- solution 2 ---------- ')
    print(solution2(num))


if __name__ == '__main__':
    main()
