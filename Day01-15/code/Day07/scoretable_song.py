#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :scoretable_song.py
# @Time      :2020/12/7 22:00
# @Author    :宋业强
def main():
    students = ["唐僧", "孙悟空", "猪八戒", "沙僧"]
    subjs = ["语文", "数学", "英语"]
    scores = [[0] * 3] * 5
    print(scores)
    for row, stu in enumerate(students):
        print("请输入%s的成绩："%stu)
        for col, sub in enumerate(subjs):
            scores[row][col] = float(input("%s："%sub))
    print(scores)


if __name__ == "__main__":
    main()
