# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：求s = a + aa + aaa + aaaa + aa...a 的值，其中a是一个数字。
     例如 2 + 22 + 222 + 2222 + 22222 (此时共有5个数相加)，几个数相加由键盘控制。
"""


def solution1(number):
    number_list = [int(str(number) * i) for i in range(1, number + 1)]
    print(sum(number_list), ' = ', ' + '.join(map(lambda i: str(i), number_list)))


def solution2(number):
    expression = ' + '.join([str(number) * i for i in range(1, number + 1)])
    print(eval(expression), ' = ', expression)


def main():
    input_str = input('输入一个数字：')
    number = 0
    try:
        number = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('---------- solution 1 ---------- ')
    solution1(number)
    print('---------- solution 2 ---------- ')
    solution2(number)


if __name__ == '__main__':
    main()
