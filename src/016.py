# !/usr/bin/python3
# -- coding: utf-8 --
"""
题目：输出指定格式的日期，常见时间、日期操作方法。
"""
import time
import calendar
import datetime

# 需要 pip 安装
from dateutil import parser


def main():
    # time 使用
    print('当前时间戳（s）：', int(time.time()))
    print('当前时间戳（ms）：', int(time.time() * 1000))
    print('当前时间（24小时制）：', time.strftime('%Y-%m-%d %H:%M:%S'))
    print('当前时间（12小时制）：', time.strftime('%Y-%m-%d %I:%M:%S'))
    print('字符串转时间：', time.strptime('2018-09-18 21:43:39', '%Y-%m-%d %H:%M:%S'))
    print('字符串转时间：', time.strptime('18 Sep 18', '%d %b %y'))

    # datetime 使用
    print('当前时间：', datetime.datetime.now())
    print('当前时间：', datetime.datetime.now().date())
    print('当前时间：', datetime.datetime.now().time())
    print('当前时间戳：', datetime.datetime.now().timestamp())
    print('UTC 时间：', datetime.datetime.utcnow())
    print('修改时间：', datetime.datetime.now().replace(day=18))
    print('字符串转时间：', datetime.datetime.strptime('2018-09-18 21:43:39', '%Y-%m-%d %H:%M:%S'))
    print('字符串转时间：', datetime.datetime.strptime('2018-09-18 21:43:39.234', '%Y-%m-%d %H:%M:%S.%f'))
    print('字符串转时间：', datetime.datetime.strptime('18 Sep 18', '%d %b %y'))
    print('算数运算：', datetime.datetime.now() - datetime.timedelta(days=1))
    print('算数运算：', datetime.datetime.now() - datetime.timedelta(hours=10))
    print('算数运算：', datetime.datetime.now() - datetime.timedelta(hours=1) * 10)
    print('算数运算：', datetime.datetime.now() - datetime.timedelta(days=1) / 24)

    # dateutil 使用
    print('字符串转时间：', parser.parse('2018-09-18 21:43:39'))
    print('字符串转时间：', parser.parse('2018/09/18 21:43:39'))
    print('字符串转时间：', parser.parse('18/09/2018 21:43:39'))
    print('字符串转时间：', parser.parse('2018-09-18 21:43:39.234'))
    print('字符串转时间：', parser.parse('18 Sep 18'))

    # calendar 使用
    print('2018 是不是闰年：', calendar.isleap(2018))
    print('2000 是不是闰年：', calendar.isleap(2000))
    print('2000 到 2018 有几个闰年：', calendar.leapdays(2000, 2018))
    print('2018年9月：', calendar.month(2018, 9))


if __name__ == '__main__':
    main()
