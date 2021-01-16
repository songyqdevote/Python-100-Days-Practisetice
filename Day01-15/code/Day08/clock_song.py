#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :clock_song.py
# @Time      :2021/1/16 10:50
# @Author    :宋业强

import time
import os

class Clock:
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            local_time = time.localtime(time.time())
            self._hour = local_time.tm_hour
            self._minute = local_time.tm_min
            self._second = local_time.tm_sec

    def run(self):
        self._second += 1
        if self._second >= 60:
            self._second = 0
            self._minute += 1
            if self._minute >= 60:
                self._minute = 0
                self._hour += 1
                if self._hour >= 23:
                    self._hour = 0


    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == "__main__":
    # clock = Clock()
    clock = Clock(hour=23,minute=59,second=60)
    while True:
        # os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()
