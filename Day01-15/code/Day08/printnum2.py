#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :printnum2.py
# @Time      :2021/6/14 20:29
# @Author    :宋业强
import threading
import time

def threada():
    with con:
        for i in range(1, 10, 2):
            time.sleep(0.2)
            print(threading.current_thread().name, i)
            con.wait()
            con.notify()


def threadb():
    with con:
        for i in range(2, 10, 2):
            time.sleep(0.2)
            print(threading.current_thread().name, i)
            con.notify()
            con.wait()

if __name__ == "__main__":
    con = threading.Condition()

    ta = threading.Thread(None, threada)
    tb = threading.Thread(None, threadb)

    ta.start()
    tb.start()
