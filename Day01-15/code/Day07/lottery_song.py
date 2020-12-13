#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lottery_song.py
# @Time      :2020/12/6 17:58
# @Author    :宋业强

from random import randrange, randint

def random_select():
    red_balls = [x for x in range(1, 34)]
    # print(red_balls)
    select_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        select_balls.append(red_balls[index])
        del red_balls[index]
    select_balls.sort()

    select_balls.append(randint(1, 16))
    # print(select_balls)
    return  select_balls

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" %ball, end=" ")
    print()


if __name__ == "__main__":
    n = int(input("机选几注；"))
    for _ in range(n):
        display(random_select())
