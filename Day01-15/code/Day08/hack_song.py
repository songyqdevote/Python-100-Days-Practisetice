#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :hack_song.py
# @Time      :2021/1/16 14:43
# @Author    :宋业强

def set_name(self, name):
    self._name = name

def show(self, course):
    print('%s正在学习%s' %(self._name, course))

if __name__ == "__main__":
    Student = type('Student', (object,), dict(__init__=set_name, study=show))
    stu = Student('wang')
    stu.study("yuwen")
