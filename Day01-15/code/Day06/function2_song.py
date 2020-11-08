#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :function2_song.py
# @Time      :2020/11/8 10:06
# @Author    :宋业强
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for i in range(x, 1, -1):
        if y % i == 0 and x % i == 0:
            return i
    else:
        return 1


def fcm(x, y):
    return x * y / gcd(x, y)

if __name__ == "__main__":
    print(gcd(12, 16))
    print(fcm(12,16))
