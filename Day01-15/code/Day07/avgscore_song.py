#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :avgscore_song.py
# @Time      :2020/11/22 20:56
# @Author    :宋业强

def avg():
    numbers = int(input("请输入考生人数："))
    students = [None] * numbers
    scorces = [None] * numbers
    for index in range(numbers):
        students[index] = input("请输入第%d学生的姓名：" %(index+1))
        scorces[index] = float(input("请输入第%d学生的分数:" %(index+1)))
    total = 0
    for index in range(numbers):
        print("学生%s的成绩为：%0.2f" %(students[index],scorces[index]))
        total += scorces[index]
    print("平均分为：%0.2f:"%(total/numbers))

if __name__ == "__main__":
    avg()
