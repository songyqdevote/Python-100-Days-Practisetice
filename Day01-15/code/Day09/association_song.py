#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :association_song.py
# @Time      :2021/6/20 11:52
# @Author    :宋业强

from math import sqrt
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x -other._x
        dy = self._y - other._y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' %(str(self._x), str(self._y))

class Line:
    def __init__(self, start=Point(0, 0), end=Point(0, 0)):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    @property
    def distance(self):
        print(self._start, self._end)
        return self._start.distance_to(self._end)


if __name__ == "__main__":
    p0 = Point(0, 0)
    p1 = Point(1, 1)
    print(p1)
    p2 = Point(-2, -2)
    print(p2)
    p2.move_by(-3, -3)
    print(p2)
    line1 = Line(p0, p2)
    print(line1.distance)
    line1.start = Point(6, 6)
    print(line1.distance)

