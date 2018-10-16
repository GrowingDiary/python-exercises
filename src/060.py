# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：打印出杨辉三角形。
"""


def solution1(height):
    values = [[0] * (height * 2 - 1) for i in range(height)]
    for i in range(height):
        values[i][height - i - 1] = 1
        values[i][height + i - 1] = 1

    for i in range(2, height):
        for j in range(height - i + 1, height - 2 + i, 2):
            values[i][j] = values[i - 1][j - 1] + values[i - 1][j + 1]

    for i in range(height):
        for j in range(height * 2 - 1):
            print('{:^4}'.format('' if values[i][j] == 0 else values[i][j]),
                  end='')
        print()


def solution2(height):
    format_str = '{{:^{length}}}'.format(length=height * 4)
    print(format_str.format('1'))
    for i in range(2, height + 1):
        s = 1
        print_str = '{:^4}'.format('1')
        for j in range(1, i - 1):
            s = (i - j) * s // j
            print_str += '{:^4}'.format(s)
        print_str += '{:^4}'.format('1')
        print(format_str.format(print_str))


def main():
    input_str = input('输入高度：')
    try:
        height = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('---------- solution 1 ---------- ')
    solution1(height)
    print('---------- solution 2 ---------- ')
    solution2(height)


if __name__ == '__main__':
    main()
