# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：暂停一秒输出，并格式化当前时间。
"""
import time
import datetime


def solution1():
    time.sleep(1)


def solution2():
    import threading
    timer = threading.Timer(1, lambda: print('现在的时间：',
                                             datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))
    timer.run()


def main():
    print('---------- solution 1 ---------- ')
    print('现在的时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    solution1()
    print('现在的时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    print('---------- solution 2 ---------- ')
    print('现在的时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    solution2()


if __name__ == '__main__':
    main()
