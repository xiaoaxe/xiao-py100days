#!/usr/bin/env python
# encoding: utf-8

"""
@description: 认识Python

@author: baoqiang
@time: 2019-05-23 22:20
"""

import sys
import turtle

# 单行注释

"""
这是多行注释
"""


def sys_info():
    a = sys.version  # str
    b = sys.version_info  # class

    print(a)
    print(b)


def plot():
    # turtle.width(4)
    turtle.pensize(4)  # 画笔宽度
    turtle.pencolor('red')

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

    # turtle.done()
    turtle.mainloop()  # 主事件循环


if __name__ == '__main__':
    # sys_info()
    plot()
