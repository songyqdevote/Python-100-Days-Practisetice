#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :list_song.py
# @Time      :2020/12/6 17:13
# @Author    :宋业强

"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素
"""
def fib(n):
    for _ in range(n):
        a, b = b, a+b
        yield a

def main():
    # gen = fib(20)
    # print(gen)
    # for elem in gen:
    #     print(elem, end=' ')
    # print()
    f = [m+n for m in "ABCDEFG"  for n in"123456"]
    print(f)

    ltest1 = ["apple", "table", "desk", "fat"]
    ltest2 =ltest1.copy()
    ltest3 = ltest1 + ltest2
    print(ltest2)
    print(ltest3)
    print(len(ltest2))
    ltest3.sort()
    print(ltest3)
    ltest3.reverse()
    print(ltest3)
    ltest4 = sorted(ltest3, reverse=True)
    ltest4 = sorted(ltest3, reverse=True)
    print(ltest4)
    # print(ltest1)
    # print(ltest1[0])
    # print(ltest1[-1])
    # print(ltest1[:])
    # for item in ltest1:
    #     print(item)
    # ltest1.append("feel")
    # ltest1.pop(0)
    # print(ltest1)
    # ltest1.insert(0, "apple")
    # print(ltest1)
    # ltest1.pop()
    # print(ltest1)


if __name__ == "__main__":
    main()
