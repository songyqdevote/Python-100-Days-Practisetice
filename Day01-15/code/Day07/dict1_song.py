#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :dict1_song.py
# @Time      :2020/12/4 20:28
# @Author    :宋业强

def main():
    scores = {"songyq":98, "wangx":99, "xx":55}
    print(scores["songyq"])
    for item in  scores:
        print(item, scores[item])
    scores.popitem()
    for k, v in scores.items():
        print(k, v)
    for k in scores.keys():
        print(k)

    for v in scores.values():
        print(v)
    print("len", len(scores))
    scores.update(小狗=50)
    print(scores)
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()
