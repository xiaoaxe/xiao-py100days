#!/usr/bin/env python
# encoding: utf-8

"""
@description: 练习题

@author: baoqiang
@time: 2019-05-24 13:33
"""

import time
import math

from random import randint

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少
"""


def run_chicken():
    """
    公鸡: 0只, 母鸡: 25只, 小鸡: 75只
    公鸡: 4只, 母鸡: 18只, 小鸡: 78只
    公鸡: 8只, 母鸡: 11只, 小鸡: 81只
    公鸡: 12只, 母鸡: 4只, 小鸡: 84只
    :return:
    """
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 1
"""


def run_perfect():
    """
    1
    6
    28
    496
    8128
    执行时间: 0.065168 秒
    :return:
    """
    # start = time.process_time()
    start = time.perf_counter()

    for num in range(1, 10000):
        sum = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum += factor
                if 1 < factor != num / factor:
                    sum += num / factor

        if sum == num:
            print(num)

    # end = time.process_time()
    end = time.perf_counter()

    print("执行时间:", (end - start), "秒")


"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""


def fibonacci():
    """
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
    :return:
    """
    a, b = 0, 1

    for _ in range(20):
        a, b = b, a + b
        print(a, end=' ')


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""


def lily():
    """
    153
    370
    371
    407
    :return:
    """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100

        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""


def craps():
    money = 1000

    while money > 0:
        print('你的总资产为:', money)
        need_go_on = False

        while True:
            debt = int(input("请下注: "))
            if 0 < debt <= money:
                break

        first = randint(1, 6) + randint(1, 6)
        print("玩家摇出了%d点" % first)

        if first == 7 or first == 11:
            print("玩家胜!")
            money += debt
        elif first in [2, 3, 12]:
            print("庄家胜!")
            money -= debt
        else:
            need_go_on = True

        while need_go_on:
            current = randint(1, 6) + randint(1, 6)
            print("玩家摇出了%d点" % current)

            if current == 7:
                print("庄家胜!")
                money -= debt
                need_go_on = False
            elif current == first:
                print("玩家胜!")
                money += debt
                need_go_on = False

    print('你破产了, 游戏结束!')


if __name__ == '__main__':
    # run_chicken()
    # run_perfect()
    # fibonacci()
    # lily()
    craps()
