# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""


def bubble_sort(*numbers):
    """
    冒泡排序
    1. 将整个待排序的记录序列划分成有序区和无序区，初始状态有序区为空，无序区包括所有待排序的记录；
    2. 对无序区从前向后依次将相邻记录的关键码进行比较，若反序则交换，从而使得关键码小的记录向前移，关键码大的记录向后移；
    3. 重复执行第 2 步，直到无序区中没有反序的记录；
    """
    result = list(numbers)
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(*numbers):
    """
    选择排序
    每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
    """
    result = list(numbers)
    for i in range(len(result)):
        min_pos = i
        for j in range(i, len(result)):
            if result[min_pos] > result[j]:
                min_pos = j
        result[i], result[min_pos] = result[min_pos], result[i]
    return result


def insertion_sort(*numbers):
    """
    插入排序
    1. 将整个待排序的记录序列划分成有序区和无序区，初始时有序区为待排序记录序列中的第一个记录，无序区包括所有剩余待排序的记录；
    2. 将无序区的第一个记录插入到有序区的合适位置中，从而使无序区减少一个记录，有序区增加一个记录；
    3. 重复执行第 2 步，直到无序区中没有记录为止；
    """
    result = list(numbers)
    for i in range(1, len(result)):
        insert_pos = i
        for j in range(i, -1, -1):
            if result[j] >= result[i]:
                insert_pos = j
            else:
                break

        if insert_pos == i:
            continue

        val = result[i]
        result[insert_pos + 1:i + 1] = result[insert_pos:i]
        result[insert_pos] = val

    return result


def quick_sort(*numbers):
    """
    快速排序
    1. 初始化：取第一个记录作为基准，设置两个参数 i，j 分别用来指示将要与基准记录进行比较的左侧记录位置和右侧记录位置，
       也就是本次划分的区间；
    2. 右侧扫描过程：将基准记录与 j 指向的记录进行比较，如果 j 指向记录的关键码大，则 j 前移一个记录位置。重复右侧扫描过程，
       直到右侧的记录小（即反序），若 i < j，则将基准记录与 j 指向的记录进行交换；
    3. 左侧扫描过程：将基准记录与 i 指向的记录进行比较，如果 i 指向记录的关键码小，则 i 后移一个记录位置。重复左侧扫描过程，
       直到左侧的记录大（即反序），若 i < j，则将基准记录与 i 指向的记录进行交换；
    4. 重复第 2，3 步，直到 i 与 j 指向同一位置，即基准记录最终位置；
    """
    def partition(num, start, end):
        while start < end:
            while start < end and num[start] < num[end]:
                end -= 1

            if start < end:
                num[start], num[end] = num[end], num[start]
                start += 1

            while start < end and num[start] < num[end]:
                start += 1

            if start < end:
                num[start], num[end] = num[end], num[start]
                end -= 1
        return start, num

    def run_sort(result, i, j):
        if i < j:
            k, result = partition(result, i, j)
            result = run_sort(result, i, k - 1)
            result = run_sort(result, k + 1, j)
        return result

    return run_sort(list(numbers), 0, len(numbers) - 1)


def solution1(*numbers):
    result = list(numbers)
    result.sort()
    return result


def solution2(*numbers):
    return sorted(numbers)


def sort_solution():
    numbers = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print('冒泡排序：', bubble_sort(*numbers))
    print('选择排序：', selection_sort(*numbers))
    print('插入排序：', insertion_sort(*numbers))
    print('快速排序：', quick_sort(*numbers))


def main():
    input_x = input('输入第一个数字：')
    input_y = input('输入第二个数字：')
    input_z = input('输入第三个数字：')
    try:
        input_x = int(input_x)
        input_y = int(input_y)
        input_z = int(input_z)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('数字顺序：', solution1(input_x, input_y, input_z))
    print('数字顺序：', solution2(input_x, input_y, input_z))
    print('数字顺序（冒泡排序）：', bubble_sort(input_x, input_y, input_z))
    print('数字顺序（选择排序）：', bubble_sort(input_x, input_y, input_z))
    print('数字顺序（插入排序）：', bubble_sort(input_x, input_y, input_z))
    print('数字顺序（快速排序）：', bubble_sort(input_x, input_y, input_z))


if __name__ == '__main__':
    main()
