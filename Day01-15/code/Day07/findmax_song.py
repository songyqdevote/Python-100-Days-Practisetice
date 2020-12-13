#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :findmax_song.py
# @Time      :2020/12/6 15:44
# @Author    :宋业强

def main():
    fruits =  ["apple", "potato", "grape", "banana"]
    print(max(fruits))
    print(min(fruits))

    max_value = min_value = fruits[0]

    for index in range(1, len(fruits)):
        if max_value < fruits[index]:
            max_value = fruits[index]
        elif min_value > fruits[index]:
            min_value = fruits[index]
    print("max", max_value)
    print("min", min_value)


if __name__ == "__main__":
    main()
