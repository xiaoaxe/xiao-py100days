#!/usr/bin/env python
# encoding: utf-8

"""
@description: class

@author: baoqiang
@time: 2019-05-24 20:19
"""

from math import sqrt
from time import localtime, time, sleep


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "(%s, %s)" % (str(self.x), str(self.y))


def run_point():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # ！！！类方法！！！
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1

            if self._minute == 60:
                self._minute = 0
                self._hour += 1

                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return "%02d:%02d:%02d" % (self._hour, self._minute, self._second)


def run_clock():
    # clock = Clock(23, 59, 59)
    clock = Clock.now()
    while True:
        print(clock.show())

        sleep(1)
        clock.run()


if __name__ == '__main__':
    run_clock()
    # run_point()
