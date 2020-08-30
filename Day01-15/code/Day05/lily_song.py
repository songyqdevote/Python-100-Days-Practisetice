#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lily_song.py
# @Time      :2020/8/30 20:47
# @Author    :宋业强


if __name__ == "__main__":
    for number in range(100, 1000):
        last = number % 10
        mid = number // 10 % 10
        first = number // 100
        if last**3 + mid**3 + first**3 == number:
            print(number, end=" ")
