#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2021/6/6 16:04
# @Author    :宋业强
def index_words(text):
    result = []
    if text:
        result.append(0)

    for index,letter in enumerate(text,1):
        print(letter)
        if letter == " ":
            result.append(index)
    return result

def num():
    print([lambda x:i*x for i in range(4)])
    return [lambda x:i*x for i in range(4)]



if __name__ == "__main__":
    for m in num():
        print(m(0))
    print([m(2) for m in num()])

