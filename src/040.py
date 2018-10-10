# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：模仿静态变量的用法。
"""


class StaticMember:
    static_member = []
    static_number = 0

    def __init__(self):
        self.class_member = []

    def __str__(self):
        return 'static member: ' + ','.join(self.static_member) + ', ' + \
               'class member: ' + ','.join(self.class_member) + ', ' + \
               'static number: ' + str(self.static_number)

    def add(self):
        self.static_member.append('a')
        self.class_member.append('b')


def solution1():
    a = StaticMember()
    b = StaticMember()
    c = StaticMember()

    a.add()
    a.static_number += 1
    print(a)
    print(b)
    print(c)
    print()

    b.add()
    StaticMember.static_number += 2
    b.static_number += 1
    print(a)
    print(b)
    print(c)
    print()

    c.add()
    StaticMember.static_number += 2
    print(a)
    print(b)
    print(c)
    print()


def main():
    print('---------- solution 1 ---------- ')
    solution1()


if __name__ == '__main__':
    main()
