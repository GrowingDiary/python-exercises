# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：打印出如下图案（菱形）:
        *
       ***
      *****
     *******
      *****
       ***
        *
"""


def solution1(h):
    max_length_line = (h + 1) // 2
    total_length = 2 * max_length_line - 1
    format_str = '{:^' + str(total_length) + '}'
    for i in range(1, max_length_line + 1):
        print(format_str.format('*' * (2 * i - 1)))
    for i in range(max_length_line, h):
        print(format_str.format('*' * ((h - i) * 2 - 1)))


def solution2(h):
    lengths = list(map(lambda i: i * 2 - 1, [x if x <= (h + 1) // 2 else h - x + 1 for x in range(1, h + 1)]))
    for l in lengths:
        print('{{:^{length}}}'.format(length=max(lengths)).format('*' * l))


def main():
    input_str = input('输入菱形的高度：')
    h = 0
    try:
        h = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    solution1(h)
    print('---------- solution 2 ---------- ')
    solution2(h)


if __name__ == '__main__':
    main()
