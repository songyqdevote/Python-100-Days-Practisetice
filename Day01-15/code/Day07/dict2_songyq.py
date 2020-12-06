#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :dict2_songyq.py
# @Time      :2020/12/6 12:09
# @Author    :宋业强

def main():
    stu = {"name": "songyq", "age": 31, "gener":True}
    print("stu1:", stu)
    print("stu.key", stu.keys())
    print("stu.value", stu.values())
    print("stu.item", stu.items())
    stu.setdefault("gener", "male")
    print("stu2:", stu)
    for item in stu.items():
        print("item", item)
        print(item[0], item[1])
    stu.setdefault("score",100)
    print("stu3:", stu)
    if "age" in stu:
        stu.update(age=28)
    print("stu4:", stu)
    stu["score"] = 99
    print("stu5:", stu)


if __name__ == "__main__":
    main()
