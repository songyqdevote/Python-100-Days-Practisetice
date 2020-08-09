#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rolldice_song.py
# @Time      :2020/8/9 15:01
# @Author    :宋业强
from random import randint

def rolldice():
    """随机菜单"""
    choice = randint(1,3)
    print(choice)
    if choice == 1:
        print("唱首歌")
    elif choice == 2:
        print("跳个舞")
    else:
        print("学狗叫")


if __name__ == "__main__":
    rolldice()
