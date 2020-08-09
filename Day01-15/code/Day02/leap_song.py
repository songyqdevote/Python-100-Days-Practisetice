#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :leap_song.py
# @Time      :2020/8/8 21:04
# @Author    :宋业强

def is_leap(year):
    """是否闰年判断"""
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(is_leap)

if __name__ == "__main__":
    year = int(input("请输入年份："))
    is_leap(year)

