#!/usr/bin/env python
# encoding: utf-8

"""
@description: 运算符

@author: baoqiang
@time: 2019-05-24 11:13
"""

import pyspark
from attr import dataclass
from pyspark.sql import Row
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType
import os
import pandas as pd

os.environ["PYSPARK_PYTHON"] = "/usr/local/bin/python3"

"""
计算机硬件5大部分组成：运算器，控制器，存储器，输入设备，输出设备
"""


def operator():
    a = 5
    b = 2

    print(a // b)  # 整除，抹掉余数
    print(a % b)  # 取余数
    print(a ** b)  # 指数运算


def operator2():
    a = 5  # 101
    b = 3  # 011
    c = ~a  # 按位取反，负数就是按位取反再加1
    d = a ^ b  # 按位异或，相同是0不同是1
    print(c)
    print("")
    print(d)


def operator3():
    """
    10001
    21
    17
    11
    0x11
    0X11

    0b10001
    0o21
    0x11


    :return:
    """

    flag = True

    if flag:
        c10 = 17
        c2 = 0b10001
        c8 = 0o21
        c16 = 0x11

        print(c10 == c2)
        print(c10 == c8)
        print(c10 == c16)

        # print(int(f'{c2}', base=2))
        print(int('0b10001', base=2))
        print(bin(-6))

    else:
        a = 17
        print('{:b}'.format(a))
        print('{:o}'.format(a))
        print('{:d}'.format(a))
        print('{:x}'.format(a))
        print('{:#x}'.format(a))
        print('{:#X}'.format(a))

        b = 17
        print(bin(b))
        print(oct(b))
        print(hex(b))

        c10 = 17
        c2 = 0b10001
        c8 = 0o21
        c16 = 0x11

        print(c10 == c2)
        print(c10 == c8)
        print(c10 == c16)


def ipt():
    a = input("请输入第一个数字: ")
    b = input("请输入第二个数字: ")

    print('{}+{}={}'.format(a, b, int(a) + int(b)))


class A:
    pass


def unreal():
    """
    <class 'int'>
    <class 'complex'>
    <class 'str'>
    <class 'tuple'>
    <class 'list'>
    <class 'dict'>
    <class 'set'>
    <class 'type'>
    :return:
    """
    print(type(1))
    print(type(1 + 2j))
    print(type(""))
    print(type(()))
    print(type([]))
    print(type({}))
    print(type(set()))
    print(type(A))


def chr_ord():
    """
    23567
    小
    \u5c0f

    128516
    
    \U0001f604

    :return:
    """
    # c = 'a'
    c = '小'
    # c = ''
    n = ord(c)
    print(n)

    c2 = chr(n)
    print(c2)

    # char to unicode
    uni = c.encode('unicode-escape').decode('ASCII')
    print(uni)


# sc = pyspark.SparkContext()
# sq = SQLContext(sc)

sc = None
sq = None


def multi_line():
    """
    使用括号进行文件折行
    :return:
    """

    rdd = sc.parallelize([1, 2, 4])
    # row_rdd = rdd.map(lambda x: Row(x))

    res_rdd = (rdd.filter(lambda x: x < 3)
               .map(lambda x: x * x)
               .map(lambda x: 'num: {}'.format(x))
               .map(lambda x: Row(x)))

    # df = sqlCtx.createDataFrame(row_rdd, ['numbers'])
    df = sq.createDataFrame(res_rdd, ['numbers'])

    df.show()


@dataclass
class Student:
    id: int
    name: str
    age: int

    def to_dict(self):
        dic = {}

        for k, v in self.__dict__.items():
            if k.startswith('__'):
                continue
            dic[k] = v

        return dic


def rdd_df():
    df = sq.createDataFrame([1, 2, 4], IntegerType())

    df.show()


def rdd_df2():
    """
    rdd: 只能map reduce和常用操作
    dataframe: 可以结合sql操作, 每一个行类型都是Row的dataset
    dataset: 每一个record都固定类型和字段的dataframe
    :return:
    """

    datas = [
        Student(1, "bao", 18),
        Student(2, "yu", 16),
    ]

    # ndarray or structured list to df
    df = pd.DataFrame.from_records([s.to_dict() for s in datas])

    ddf = sq.createDataFrame(df)

    for row in ddf.collect():
        print(row['id'], row['name'], row['age'])

    #
    # pd.DataFrame.from_dict()

    # list of tuples to df
    # pd.DataFrame.from_items()


if __name__ == '__main__':
    # operator()
    # unreal()
    # chr_ord()
    # multi_line()
    # rdd_df()
    # rdd_df2()
    # operator2()
    operator3()
    # ipt()
