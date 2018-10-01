# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
     Sunday Monday Tuesday Wednesday Thursday Friday Saturday
     0      1      2       3         4        5      6
"""


def solution1():
    input_str = ''
    while True:
        input_str += input('输入一个字符：').lower()
        if input_str == 'm':
            return 'Monday'
        if input_str == 'w':
            return 'Wednesday'
        if input_str == 'f':
            return 'Friday'
        if input_str in ('s', 't'):
            continue
        if input_str == 'su':
            return 'Sunday'
        if input_str == 'sa':
            return 'Saturday'
        if input_str == 'tu':
            return 'Tuesday'
        return 'Thursday'


def solution2():
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday']
    for i in range(2):
        input_str = input('输入一个字符：').lower()
        weekdays = [x for x in weekdays if x[i] == input_str]
        if len(weekdays) == 1:
            return weekdays[0]


def main():
    print('---------- solution 1 ---------- ')
    print(solution1())
    print('---------- solution 2 ---------- ')
    print(solution2())


if __name__ == '__main__':
    main()
