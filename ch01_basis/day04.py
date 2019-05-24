#!/usr/bin/env python
# encoding: utf-8

"""
@description: 循环语句

@author: baoqiang
@time: 2019-05-24 12:58
"""

import dis


def int_cache():
    """
    [-5,256], 缓存的实例对象，内存中只有一份
    x is not y: -6
    x is not y: 257
    :return:
    """

    x = -7
    y = -7

    while x <= 256:
        x += 1
        y += 1

        if x is not y:
            print('x is not y: {}'.format(x))


# a = 257
a = -2333.3


def scope_cache():
    """
    不同作用域会新建不同对象，相同作用域使用同一个对象
    对str，浮点数，整数都成立
    :return:
    """
    # b = 257
    # c = 257

    b = -2333.3
    c = -2333.3

    print(b is a)  # False
    print(b is c)  # True


def nesting_list():
    """
    嵌套列表的初始化
    :return:
    """

    # mylist = [[0] * 3] * 5 # error
    mylist = [[0 for _ in range(3)] for _ in range(5)]

    for i in range(5):
        for j in range(3):
            mylist[i][j] = '{}-{}'.format(i + 1, j + 1)

    print(mylist)


def public_private():
    """
    单下划线开头，声明我是私有变量，希望不要被访问和修改，可以被继承
    双下划线开头，语言层面保证是私有，不能被继承，不过可以magic访问到，ins._cls__name
    :return:
    """


if __name__ == '__main__':
    # int_cache()
    # scope_cache()
    # dis.dis(scope_cache)
    nesting_list()
