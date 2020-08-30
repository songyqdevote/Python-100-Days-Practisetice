#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :for1_song.py
# @Time      :2020/8/21 21:52
# @Author    :宋业强
def sum (x):
    s = 0
    for i in range(x + 1):
        s += i
    print("s", s)

if __name__ == "__main__":
    x = int(input("请输入一个数"))
    sum(x)
