# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：企业发放的奖金根据利润提成。
     利润(I)低于或等于10万元时，奖金可提10%；
     利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
     20万到40万之间时，高于20万元的部分，可提成5%；
     40万到60万之间时高于40万元的部分，可提成3%；
     60万到100万之间时，高于60万元的部分，可提成1.5%；
     高于100万元时，超过100万元的部分按1%提成。
     从键盘输入当月利润I，求应发放奖金总数？
"""


def solution1(profit):
    if profit <= 10:
        return profit * 0.1
    if 10 < profit <= 20:
        return 0.1 * 10 + (profit - 10) * 0.075
    if 20 < profit <= 40:
        return 0.1 * 10 + 0.075 * 10 + (profit - 20) * 0.05
    if 40 < profit <= 60:
        return 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + (profit - 40) * 0.03
    if 60 < profit <= 100:
        return 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + 0.03 * 20 + (profit - 60) * 0.015
    if profit > 100:
        return 0.1 * 10 + 0.075 * 10 + 0.05 * 20 + 0.03 * 20 + 0.015 * 40 + (profit - 100) * 0.01


def solution2(profit):
    percentage = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    floor_profit = [100, 60, 40, 20, 10, 0]

    generate_list = []
    for i in range(len(floor_profit)):
        if profit > floor_profit[i]:
            generate_list = [floor_profit[j] - floor_profit[j + 1]
                             for j in range(i, len(floor_profit)) if j + 1 < len(floor_profit)]
            generate_list.reverse()
            generate_list.append(profit - floor_profit[i])
            break

    return sum(list(map(lambda x, y: x * y, percentage[:len(generate_list)], generate_list)))


def main():
    input_str = input('输入利润提成（万元）：')
    try:
        profit = int(input_str)
    except Exception as e:
        print('Exception', repr(e))
        return

    print('奖金（万元）：', solution1(profit))
    print('奖金（万元）：', solution2(profit))


if __name__ == '__main__':
    main()
