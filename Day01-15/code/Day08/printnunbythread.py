#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :printnunbythread.py
# @Time      :2021/6/14 17:21
# @Author    :宋业强

"""
创建两个线程打印1-1000，一个线程打印奇数，一个线程打印偶数
入参：无
输出：
"""


import threading
import time

#打印奇数
def print_odd(num):
    for i in range(1, num+1):
        if i % 2 != 0:
            lock_even.acquire()
            print(threading.current_thread().name, i)
            lock_odd.release()
            time.sleep(0.1)

#打印奇数
def print_even(num):
    for i in range(1, num+1):
        if i % 2 == 0:
            lock_odd.acquire()
            print(threading.current_thread().name, i)
            lock_even.release()
            time.sleep(0.1)




if __name__ == "__main__":
    # num = 1000
    num = int(input("Please input an integer："))
    lock_odd = threading.Lock()
    lock_even = threading.Lock()

    thread_odd = threading.Thread(target=print_odd, args=(num,))
    thread_even = threading.Thread(target=print_even, args=(num,))
    lock_odd.acquire()
    thread_odd.start()
    thread_even.start()

