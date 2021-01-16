#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rect_song.py
# @Time      :2021/1/16 15:00
# @Author    :宋业强

class Rect:
    def __init__(self,width = 0, length = 0):
        self._width = width
        self._length = length

    def area(self):
        return self._width * self._length

    def __str__(self):
        return '矩形[%.2f,%.2f]'% (self._length, self._width)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')

if __name__ == "__main__":
    rect1 = Rect()
    print(rect1)
    print(rect1.area())
