#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :guess_song.py
# @Time      :2020/8/30 17:28
# @Author    :宋业强
from random import randint

if __name__ == "__main__":
    count = 0
    answer = randint(1, 100)

    while True:
        count += 1
        num = int(input("请输入一个数:"))
        if num < answer:
            print("你猜小了")
        elif num > answer:
            print("你猜大了")
        else:
            print("你太聪明了猜对了")
            break
        if count > 7:
            print("你太笨了，猜了7次了")
            break