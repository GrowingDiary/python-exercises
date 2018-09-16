# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""


def solution1(y, m, d):
    is_leap_year = (y % 4 == 0)
    month_31_days = {1, 3, 5, 7, 8, 10, 12}
    day_count = d
    if m > 2:
        day_count += (29 if is_leap_year else 28)

    day_count += sum([31 if x in month_31_days else 30 for x in range(1, m) if x != 2])
    return day_count


def solution2(y, m, d):
    import datetime
    return datetime.datetime(year=y, month=m, day=d).timetuple().tm_yday


def main():
    input_year = input('输入日期（年）：')
    input_month = input('输入日期（月）：')
    input_day = input('输入日期（日）：')
    try:
        input_year = int(input_year)
        input_month = int(input_month)
        input_day = int(input_day)
    except Exception as e:
        print('Exception', repr(e))
        return

    day_count1 = solution1(y=input_year, m=input_month, d=input_day)
    print('{y}-{m}-{d} 是今年的第 {n} 天'.format(y=input_year, m=input_month, d=input_day, n=day_count1))
    day_count2 = solution2(y=input_year, m=input_month, d=input_day)
    print('{y}-{m}-{d} 是今年的第 {n} 天'.format(y=input_year, m=input_month, d=input_day, n=day_count2))


if __name__ == '__main__':
    main()
