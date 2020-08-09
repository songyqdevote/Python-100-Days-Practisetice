#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conversion_song.py
# @Time      :2020/8/9 10:55
# @Author    :宋业强

def convertion(value):
    """英制英寸与公制厘米转换"""
    unit = input("请输入单位")
    if unit == "in" or unit =="英寸":
        print("输入的长度为%.2f英寸，%.2f厘米" %(value, value*2.54))
    elif unit == "cm" or unit == "厘米":
        print("输入的长度为%.2f英寸，%.2f厘米" %(value/2.54, value))
    else:
        print("请输入正确的单位")

if __name__ == "__main__":
    value = float(input("请输入长度"))
    convertion(value)
