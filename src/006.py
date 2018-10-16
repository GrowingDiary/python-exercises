# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：斐波那契数列
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""


def solution1(length):
    fibonacci_seq = []
    for i in range(length):
        if i < 2:
            fibonacci_seq.append(1)
            continue
        fibonacci_seq.append(sum(fibonacci_seq[-2:]))
    return fibonacci_seq


def solution2(length):
    # Binet's Fibonacci number formula
    # http://mathworld.wolfram.com/FibonacciNumber.html
    def fibonacci(n):
        return int(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (2 ** n * 5 ** 0.5))

    return list(map(fibonacci, range(1, length + 1)))


def main():
    input_str = input('输入生成数列的长度：')
    try:
        length = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return
    print('---------- solution 1 ---------- ')
    print('Fibonacci sequence:', solution1(length))
    print('---------- solution 2 ---------- ')
    print('Fibonacci sequence:', solution2(length))


if __name__ == '__main__':
    main()
