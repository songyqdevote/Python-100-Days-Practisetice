#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :print_num_thread.py
# @Time      :2021/6/16 18:15
# @Author    :宋业强

"""
创建两个线程打印1-1000，一个线程打印奇数，一个线程打印偶数
入参：正整数
输出：一个线程打印奇数，一个线程打印偶数
"""

import threading
import time


# 打印奇数
def print_odd(num):
    if not isinstance(num, int):
        print("Please input a positive integer!!!")
    else:
        if num <= 0:
            print("Please input a positive integer!!!")
        else:
            for i in range(1, num + 1):
                if i % 2 != 0:
                    lock_even.acquire()
                    print(threading.current_thread().name, i)
                    lock_odd.release()
                    # time.sleep(0.1)


# 打印偶数
def print_even(num):
    if not isinstance(num, int):
        print("Please input a positive integer!!!")
    else:
        if num <= 0:
            print("Please input a positive integer!!!")
        else:
            for i in range(1, num + 1):
                if i % 2 == 0:
                    lock_odd.acquire()
                    print(threading.current_thread().name, i)
                    lock_even.release()
                    # time.sleep(0.1)


if __name__ == "__main__":
    # num =1000
    num_str = input("Please input a positive integer：")
    if not num_str:
        print("You input nothing,please input a positive integer!!!")
    else:

        num = int(num_str)
        if num <= 0:
            print("Please input a positive integer!!!")
        else:
            lock_odd = threading.Lock()
            lock_even = threading.Lock()
            thread_odd = threading.Thread(target=print_odd, args=(num,))
            thread_even = threading.Thread(target=print_even, args=(num,))
            lock_odd.acquire()

            thread_odd.start()
            thread_even.start()
