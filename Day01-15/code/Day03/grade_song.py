#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :grade_song.py
# @Time      :2020/8/9 11:06
# @Author    :宋业强
"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E
"""
def grade_convert(score):
    """成绩等级转换"""
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    else:
        grade = "E"
    print("输入成绩为%.1f,对应等级为%s" %(score, grade))


if __name__ == "__main__":
    score = float(input("请输入成绩分数"))
    grade_convert(score)
