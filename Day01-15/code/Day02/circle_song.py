#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :circle_song.py
# @Time      :2020/8/8 20:54
# @Author    :宋业强

import  math

def cal_circle(redius):
    """周长面积计算"""
    squre = math.pi * redius * redius
    perimeter = 2 * math.pi * redius
    print("输入半径对应圆的周长为：%.2f,面积为：%.2f" %(perimeter, squre))
if __name__ == "__main__":
    redius = float(input("请输入半径："))
    cal_circle(redius)
