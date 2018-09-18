# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：利用条件运算符的嵌套来完成此题：学习成绩 >=90 分的同学用 A 表示，60-89 分之间的用 B 表示，60 分以下的用 C 表示。
"""


def solution1(number):
    if number >= 90:
        return 'A'
    elif number >= 60:
        return 'B'
    else:
        return 'C'


def main():
    input_str = input('输入一个成绩：')
    number = 0
    try:
        number = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('---------- solution 1 ---------- ')
    print('分数：', solution1(number))


if __name__ == '__main__':
    main()
