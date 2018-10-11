# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
"""


def main():
    while True:
        input_str = input('输入数字：')
        try:
            input_num = int(input_str)
        except Exception as e:
            print('Exception', repr(e))
            return

        square = input_num ** 2
        print('平方值：', square)
        if square < 50:
            break


if __name__ == '__main__':
    main()
