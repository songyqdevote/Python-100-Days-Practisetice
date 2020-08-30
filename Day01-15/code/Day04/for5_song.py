#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :for5_song.py
# @Time      :2020/8/29 21:32
# @Author    :宋业强


if __name__ == "__main__":
    x = int(input("x = "))
    y = int(input("y = "))
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            print("最大公约数为：", i)
            print("最小公倍数", x * y / i)
            break