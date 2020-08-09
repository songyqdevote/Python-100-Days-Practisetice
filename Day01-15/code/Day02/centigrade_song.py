 #!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :centigrade_song.py
# @Time      :2020/8/8 18:24
# @Author    :宋业强

# F = 1.8C + 32

def centigrade_change(f):
    """温度转换"""
    c = (f - 32) / 1.8
    print("华氏温度：%.1f,对应的摄氏温度%.1f" %(f,c))

if __name__ == "__main__":
    f = float(input("请输入华氏温度"))
    centigrade_change(f)
