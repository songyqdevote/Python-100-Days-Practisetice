#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :for3_song.py
# @Time      :2020/8/29 15:47
# @Author    :宋业强


if __name__ == "__main__":
    n = int(input("请输入一个数："))
    mul = 1
    for i in range(1, n):
        mul *= i
    print("输入数%d的阶乘为%d" %(int(n), int(mul)))
