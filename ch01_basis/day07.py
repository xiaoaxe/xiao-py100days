#!/usr/bin/env python
# encoding: utf-8

"""
@description: str & data structure

@author: baoqiang
@time: 2019-05-24 13:34
"""

from copy import deepcopy
import string
import sys
import os
import time
import random


######

# exercise 1
def exercise():
    # marquee()
    # print(verify_code())
    # print(get_suffix("hello.txt"))
    # print(max2([5, 46, 3, 8, 2, 9, 7, 9, 6, 0, 42, 3, 6, 4, 7, 9, 2, 0]))
    # print(witch_day(2019, 3, 23))
    yanghui_triangle()


def marquee():
    """
    跑马灯
    :return:
    """
    content = '北京欢迎你为你开天辟地..........'
    while True:
        os.system("clear")
        print(content)

        time.sleep(0.2)

        content = content[1:] + content[0]


def verify_code(code_len=4):
    chars = string.digits + string.ascii_letters
    last_post = len(chars) - 1

    codes = []

    for _ in range(code_len):
        idx = random.randint(0, last_post)
        codes.append(chars[idx])

    return "".join(codes)


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        idx = pos if has_dot else pos + 1
        return filename[idx:]
    else:
        return ''


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])

    for idx in range(2, len(x)):
        if x[idx] > m1:
            m2 = m1
            m1 = x[idx]
        elif x[idx] > m2:
            m2 = x[idx]

    return m1, m2


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def witch_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]

    total = 0

    for idx in range(month - 1):
        total += days_of_month[idx]
    return total + date


def yanghui_triangle():
    num = int(input("Number of rows: "))
    yh = [[]] * num

    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)

        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]

            print(yh[row][col], end='\t')

        print()


######

def method_str():
    s = "hello"
    print(s.find('oo'))
    print(s.index('ll'))  # 找不到会抛出异常ValueError

    print(s.center(10))  # 后面比前面多一个
    print(s.rjust(10, "*"))  # 靠右边填充，前面放小星星
    # print(s.ljust(10))


def method_str2():
    s2 = 'abc123456'
    print(s2[::-1])  # 反转

    # 复制
    s3 = deepcopy(s2)
    s4 = ''.join(s2)  # it works!
    s5 = s2[:]
    print(id(s2))
    print(id(s3))
    print(id(s4))
    print(id(s5))

    # number
    print(s2.isalnum())
    print(s2.isalpha())
    print(s2.isnumeric())

    print(string.ascii_letters)
    print(string.ascii_uppercase)
    print(string.ascii_lowercase)
    print(string.digits)
    print(string.punctuation)
    print(string.whitespace)
    print(string.printable)


def list_man():
    s = [1, 2, 3]

    if 4 in s:
        s.remove(4)  # val err

    s.extend([5, 4])

    print(s)

    s2 = ['3'] * 5
    print(s2)

    # 对比str，这里创建了新的对象
    s3 = s[:]
    print(id(s))
    print(id(s3))


def list_man2():
    """
    f:9024
    g:120

    %timeit [1,2,3,4,5] : 53.7 ns
    %timeit (1,2,3,4,5) : 7.13 ns

    :return:
    """
    f = [x ** 2 for x in range(1000)]
    g = (x ** 2 for x in range(1000))

    print(sys.getsizeof(f))
    print(sys.getsizeof(g))


def set_man():
    s = {1, 2, 2, 3}
    print(len(s))

    s.update({6, 5})
    s.discard(2)
    print(s)

    for i in range(10, 100):
        s.add('{}'.format(i))

    # 随机的返回一个元素
    print(s.pop())
    print(s.pop())
    print(s)


def set_man2():
    s1 = {1, 2, 3}
    s2 = {1, 2, 4}

    print(s1.intersection(s2))  # s1 & s2
    print(s1.union(s2))  # s1 | s2
    print(s1.difference(s2))  # s1 - s2
    # 相同返回0，不同返回1
    print(s1.symmetric_difference(s2))  # s1 ^ s2
    print(s1.issubset(s2))  # s1 <= s2
    print(s1.issuperset(s2))  # s1 >= s2


def dict_man():
    dic = {
        'name': 'xiao', 'age': 18,
    }

    print(dic.popitem())
    print(dic)
    print(dic.pop('name'))
    # print(dic.pop('xiao'))
    print(dic)


if __name__ == '__main__':
    # method_str2()
    # list_man2()
    # set_man2()
    # dict_man()
    exercise()
