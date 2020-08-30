#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :palindrome_song.py
# @Time      :2020/8/30 20:59
# @Author    :宋业强


if __name__ == "__main__":
    num = int(input("请输入一个数："))
    num2 = 0
    temp = num
    while temp:
        num2 = num2 * 10 + temp %10
        temp = temp //10
    if num == num2:
        print("输入的数是回文数")
    else:
        print("输入的不是回文数")

