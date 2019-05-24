#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数

@author: baoqiang
@time: 2019-05-24 13:34
"""

import random

"""
8个苹果分给4个人，每人至少一个有多少种方案
隔板法，8个苹果中间又7个隔板，插入三块隔板
C(7,3), 第一块板有7种插法，第二块有6种，第三块有5种
"""


def explore_rand():
    for i in range(100):
        # r = random.randrange(1, 5, 2)
        # r = random.randrange(1, 5)
        # r = random.choices([1, 2, 3], k=2)
        # print(r)
        pass

    # [0,1)之间的浮点数
    print(random.random())

    # [a,b]之间的整数
    print(random.randint(1, 5))

    # [a,b]之间的浮点数,可能包含或者不包含b
    print(random.uniform(1, 5))

    # [a,b)之间的整数,如果有步长，会步长跳跃
    print(random.randrange(1, 5, 2))

    # 随机选多个，有放回的抽样
    print(random.choices([1, 2, 3], k=2))

    # 随机选多个，无放回的抽样
    print(random.sample([1, 2, 3], k=2))


def is_palindrome(num):
    temp = num

    total = 0

    # 原来数字的最后一位变为新的最高位，一直循环遍历加到原来数字最高位
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num


if __name__ == '__main__':
    explore_rand()
