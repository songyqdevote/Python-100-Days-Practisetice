#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fibonacci_song.py
# @Time      :2020/12/6 15:12
# @Author    :宋业强

def main():
    n = int(input("please input a number bigger than 2:"))
    f = [1, 1]
    for i in range(2, n):
        print(i)
        # f.append(f[i-1] + f[i-2])
        f += f[i-1] + f[i-2]
    for item in f:
        print(item, end=" ")

if __name__ == "__main__":
    main()
