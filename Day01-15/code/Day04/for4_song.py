#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :for4_song.py
# @Time      :2020/8/29 19:32
# @Author    :宋业强

from math import sqrt

if __name__ == "__main__":
    """判断输入的数是不是素数"""
    n = int(input("请输入一个数："))
    n_sqrt = int(sqrt(n))
    print(n_sqrt)
    is_prime = True
    for i in range(2, n_sqrt+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime and n != 1:
        print("输入的%d是素数" %n)
    else:
        print("输入的%d不是素数" %n)