#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :verify_song.py
# @Time      :2020/8/9 16:39
# @Author    :宋业强
import getpass
def verify(username, password):
    """身份验证"""
    if username == "admin" and password == "123456":
        print("身份正确")
    else:
        print("验证失败")


if __name__ == "__main__":
    username = input("请输入用户名")
    password = input("请输入密码")
    verify(username, password)
