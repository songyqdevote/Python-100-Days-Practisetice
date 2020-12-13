#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :yanghui_song.py
# @Time      :2020/12/13 18:01
# @Author    :宋业强

def main():
    num = int(input("请输入一个数："))
    yh = [[]] * num

    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)

        for col in range(len(yh[row])):
            if col == 0 or col == row :
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col-1] + yh[row-1][col]
            print(yh[row][col], end='\t')
        print()
    print(yh)


if __name__ == "__main__":
    main()
