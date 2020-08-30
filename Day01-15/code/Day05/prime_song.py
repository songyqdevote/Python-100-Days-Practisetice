#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :prime_song.py
# @Time      :2020/8/30 21:06
# @Author    :宋业强
from math import sqrt

if __name__ == "__main__":
    num = int(input("请输入一个整数："))
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0 :
            is_prime = False
            break
    if is_prime == True:
         print("你输入的%d是素数" %num)

