#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :is_triangle.py
# @Time      :2020/8/9 15:10
# @Author    :宋业强

def is_triangle(a, b, c):
    """三角形判断"""
    if a + b > c and a + c > b and b + c > a:
        print("三角形的周长", a + b + c)
    else:
        print("输入的不满足三角形")

if __name__ == "__main__":
    a = float(input("输入边长1："))
    b = float(input("输入边长2："))
    c = float(input("输入边长3："))
    is_triangle(a, b, c)
