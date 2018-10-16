# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：查找字符串。
"""


def main():
    a = 'abcdefg'

    if 'abc' in a:
        print('abc in str:', a)

    print('str:', a, 'find "def" pos:', a.find('def'))


if __name__ == '__main__':
    main()
