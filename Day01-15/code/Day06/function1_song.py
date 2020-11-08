#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :function1_song.py
# @Time      :2020/9/6 17:18
# @Author    :宋业强

def factor(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

if __name__ == "__main__":
    print(factor(9))
    print(factor(7) // factor(3) // factor(4))
