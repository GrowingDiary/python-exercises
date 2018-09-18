# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：暂停一秒输出。
"""
import time


def solution1():
    time.sleep(1)


def solution2():
    import threading
    timer = threading.Timer(1, lambda: print('现在的时间戳（ms）：', int(time.time() * 1000)))
    timer.run()


def main():
    print('---------- solution 1 ---------- ')
    print('现在的时间戳（ms）：', int(time.time() * 1000))
    solution1()
    print('现在的时间戳（ms）：', int(time.time() * 1000))
    print('---------- solution 2 ---------- ')
    print('现在的时间戳（ms）：', int(time.time() * 1000))
    solution2()


if __name__ == '__main__':
    main()
