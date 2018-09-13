# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""


def solution1(input_list, n):
    import itertools
    return list(itertools.permutations(input_list, n))


def solution2(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def main():
    print('---------- solution 1 ---------- ')
    output_list = list(solution1(range(1, 5), 3))
    print('permutations count:', len(output_list))
    print('permutations:', output_list)

    print('---------- solution 2 ---------- ')
    output_list = list(solution2(range(1, 5), 3))
    print('permutations count:', len(output_list))
    print('permutations:', output_list)


if __name__ == '__main__':
    main()
