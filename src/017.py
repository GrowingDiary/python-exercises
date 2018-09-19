# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


def solution1(input_str):
    char_count = 0
    blank_count = 0
    num_count = 0
    else_count = 0
    for i in input_str:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            char_count += 1
            continue
        if i == ' ':
            blank_count += 1
            continue
        if '0' <= i <= '9':
            num_count += 1
            continue
        else_count += 1
    print('char:', char_count, 'blank:', blank_count, 'number:', num_count, 'else:', else_count)


def solution2(input_str):
    char_count = 0
    blank_count = 0
    num_count = 0
    else_count = 0
    for i in input_str:
        if ord(i) in range(ord('a'), ord('z') + 1) or ord(i) in range(ord('A'), ord('Z') + 1):
            char_count += 1
            continue
        if ord(i) in range(ord('0'), ord('9') + 1):
            num_count += 1
            continue
        if i == ' ':
            blank_count += 1
            continue
        else_count += 1
    print('char:', char_count, 'blank:', blank_count, 'number:', num_count, 'else:', else_count)


def solution3(input_str):
    import string
    char_count = 0
    blank_count = 0
    num_count = 0
    else_count = 0
    for i in input_str:
        if i in string.ascii_letters:
            char_count += 1
            continue
        if i in string.digits:
            num_count += 1
            continue
        if i == ' ':
            blank_count += 1
            continue
        else_count += 1
    print('char:', char_count, 'blank:', blank_count, 'number:', num_count, 'else:', else_count)


def solution3(input_str):
    import re
    char_count = len(re.findall('[a-zA-Z]', input_str))
    blank_count = len(re.findall('\s', input_str))
    num_count = len(re.findall('[0-9]', input_str))
    else_count = len(input_str) - char_count - blank_count - num_count
    print('char:', char_count, 'blank:', blank_count, 'number:', num_count, 'else:', else_count)


def main():
    input_str = input('输入一行字符：')
    print('---------- solution 1 ---------- ')
    solution1(input_str)
    print('---------- solution 2 ---------- ')
    solution2(input_str)
    print('---------- solution 3 ---------- ')
    solution3(input_str)


if __name__ == '__main__':
    main()
