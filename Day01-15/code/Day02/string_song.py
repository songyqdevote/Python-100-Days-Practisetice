#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :string_song.py
# @Time      :2020/8/8 21:23
# @Author    :宋业强

str = "hello world!"
print("字符串长度", len(str))
print('单词首字符大写', str.title())
print('字符串转为大写', str.upper())
print('字符串是否为小写', str.islower())
print('字符串是否以hello开头', str.startswith('hello'))
str2 = '- \u9a86\u660a'
str3 = str.title() + ' ' + str2.lower()
print(str3)