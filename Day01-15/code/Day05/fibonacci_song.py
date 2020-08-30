#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fibonacci_song.py
# @Time      :2020/8/30 16:27
# @Author    :宋业强


if __name__ == "__main__":
    a, b = 0, 1
    for i in range(100):
        a, b = b, a + b
        print(a, end = " ")

