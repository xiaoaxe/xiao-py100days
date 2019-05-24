#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数

@author: baoqiang
@time: 2019-05-24 13:34
"""


def is_palindrome(num):
    temp = num

    total = 0

    # 原来数字的最后一位变为新的最高位，一直循环遍历加到原来数字最高位
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num


if __name__ == '__main__':
    pass
