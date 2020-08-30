#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chicken_song.py
# @Time      :2020/8/30 15:46
# @Author    :宋业强


if __name__ == "__main__":
    for x in range(0, 20):
        for y in range(0,33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print("公鸡%d只，母鸡%d只，小鸡%d只" %(x, y, z))
                break

