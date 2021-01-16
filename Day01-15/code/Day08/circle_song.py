#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :circle_song.py
# @Time      :2021/1/10 20:12
# @Author    :宋业强
"""
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)
"""
"""
知识点：
@property:Python的一种修饰器，用来修饰方法。
作用：可以用来创建只读属性，会将方法转换为同名的只读属性 ，防止修改
加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）
在python中定义私有变量只需要在变量名或函数名前加上 "__"两个下划线，那么这个函数或变量就会为私有的了

声明该方法为私有方法，不能在类的外部调用
在Python中，通过单下划线"“来实现模块级别的私有化，变量除外。一般约定以单下划线”"开头的函数为模块私有的，也就是说"from moduleName import * “将不会引入以单下划线”"开头的函数。
总结：
"__“和” _ __"的使用 更多的是一种规范/约定，并没有真正达到限制的目的：
“_”：以单下划线开头的表示的是protected类型的变量，即只能允许其本身与子类进行访问；同时表示弱内部变量标示，如，当使用"from moduleNmae import *"时，不会将以一个下划线开头的对象引入。
“__”：双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了，连子类也不可以，这类属性在运行时属性名会加上单下划线和类名。


"""
import math

class Circle:
    def __init__(self, redius):
        self._redius = redius

    @property
    def redius(self):
        return self._redius
    @redius.setter
    def redius(self, redius):
        self._redius = redius if redius > 0 else 0

    @property
    def area(self):
        return 2 * math.pi * self._redius

    @property
    def perimeter(self):
        return math.pi * self._redius * self._redius



if __name__ == "__main__":
    redius = float(input("请输入一个半径值："))
    small_circle = Circle(redius)
    big_circle = Circle(redius + 3)
    wall_cost = big_circle.perimeter *32.5
    street_coast = (big_circle.area - small_circle.area) * 25
    print('围墙造价为：￥%.2f元' %wall_cost)
    print("道路造价为：￥%.2f元" %street_coast)
    small_circle.redius = 9
    print(small_circle.redius)
