# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：学习使用 auto 定义变量的用法（变量作用域）。
"""


global_number = 0


def solution1():
    global_number = 1
    print('local number:', global_number)
    global_number += 1


def solution2():
    global global_number
    global_number += 1
    print('global func number', global_number)


for i in range(3):
    global_number += 1
    print('global number:', global_number)
    solution1()
    solution2()
