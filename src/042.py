# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：模仿静态变量(static)另一案例。
"""


class StaticMember:
    static_number = 0

    def add(self):
        self.static_number += 1

    def __str__(self):
        return 'static number: ' + str(self.static_number)


def main():
    static_number = 0
    static_class = StaticMember()
    for i in range(3):
        static_number += 1
        static_class.add()
        print('local: ', static_number)
        print(static_class)


if __name__ == '__main__':
    main()
