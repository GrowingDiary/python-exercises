# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输出一个随机数。
"""


def main():
    import random
    print('随机数：', random.randint(0, 100))
    print('随机数：', random.uniform(0, 100))
    print('随机数：', random.random())


if __name__ == '__main__':
    main()
