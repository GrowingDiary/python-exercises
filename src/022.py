# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：两个乒乓球队进行比赛，各出三人。
     甲队为 a, b, c 三人，乙队为 x, y, z 三人。
     已抽签决定比赛名单。
     有人向队员打听比赛的名单。
     a 说他不和 x 比，c 说他不和 x, z 比。
     请编程序找出三队赛手的名单。
"""


def solution1():
    import itertools
    for i in itertools.permutations('xyz'):
        # a 不与 x 比赛
        if i[0] == 'x':
            continue

        # c 不与 x, z 比赛
        if i[2] == 'x' or i[2] == 'z':
            continue

        print('参赛顺序：a vs {a}, b vs {b}, c vs {c}'.format(a=i[0], b=i[1], c=i[2]))


def solution2():
    a = {'y', 'z'}
    b = {'x', 'y', 'z'}
    c = {'y'}

    a = a.difference(c)
    b = b.difference(c)
    b = b.difference(a)
    print('参赛顺序：a vs {a}, b vs {b}, c vs {c}'.format(a=a.pop(), b=b.pop(), c=c.pop()))


def main():
    print('---------- solution 1 ---------- ')
    solution1()
    print('---------- solution 2 ---------- ')
    solution2()


if __name__ == '__main__':
    main()
