#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :set1_song.py
# @Time      :2020/12/9 21:42
# @Author    :宋业强
def main():
    set1 = {1, 2, "3", 4, "5"}
    print(set1)
    print("lenth=", len(set1))
    set2 = set(list(range(1, 9)))
    print("set2:", set2)
    set1.add(6)
    set1.add(4)
    set1.update([7, 8])
    set1.discard(7)
    print(set1)



if __name__ == "__main__":
    main()
