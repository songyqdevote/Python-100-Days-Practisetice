#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :find_first__difchar.py
# @Time      :2021/6/15 21:34
# @Author    :宋业强

"""
给定一个字符串，找出其中最靠前且只出现一次的字符
入参str：一个字符串
返回：如果存在则返回，如果不存在返回None
"""


def find_first_difchar(str_test):
    dic = {}
    if not str_test:
        print("Your input string is None")
        return None
    else:
        # 把字符串的字符作为字典的键，对应的字符有多少个作为值，循环处理
        if not isinstance(str_test, str):
            print("Please input a positive integer!!!")
        else:
            for i in range(len(str_test)):
                if str_test[i] in dic.keys():
                    dic[str_test[i]] += 1
                else:
                    dic[str_test[i]] = 1
            # 循环判断，找到第一个值为1的对应的键就是要找的字符，直接返回，如果不存在不同的字符返回None
            for i in range(len(str_test)):
                if dic[str_test[i]] == 1:
                    return str_test[i]
                else:
                    return None


if __name__ == "__main__":
    # str_test = input("Please input a string:")
    dict={"k":"v"}
    dif_char = find_first_difchar(dict)
    print(dif_char)
