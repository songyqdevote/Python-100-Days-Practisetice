#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :find_first__difchar.py
# @Time      :2021/6/15 21:34
# @Author    :宋业强

"""
查找字符串第一个不同的字符
入参str：一个非空字符串
返回：如果存在则返回，如果不存在返回None
"""
def find_first_difchar(str):
    dic = {}
    if not str:
        print("Your input string is None")
    else:
        #把字符串的字符作为字典的键，对应的字符有多少个作为值，循环处理
        for i in range(len(str)):
            if str[i] in dic.keys():
                dic[str[i]] += 1
            else:
                dic[str[i]] = 1
        #循环判断，找到第一个值为1的对应的键就是要找的字符，直接返回，如果不存在不同的字符返回None
        for i in range(len(str)):
            if dic[str[i]] == 1:
               return str[i]



if __name__ == "__main__":
    str = input("Please input a string:")
    dif_char = find_first_difchar(str)
    print(dif_char)
