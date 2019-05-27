#!/usr/bin/env python
# encoding: utf-8

"""
@description: regex

@author: baoqiang
@time: 2019-05-25 22:35
"""

import re

"""
\\b表示匹配文件边界
\\b的大写\\B表示不匹配单词边界，所以相应的\\W表示不匹配英语汉字和下划线
re.match可以用于匹配字符串多次
"""


def re_qq():
    username = input("请输入用户名: ")
    qq = input("请输入QQ号: ")

    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print("请输入有效的用户名")

    m2 = re.match(r'[1-9]\d{4,11}$', qq)
    if not m2:
        print("请输入有效的QQ号.")

    if m1 and m2:
        print("你输入的信息是有效的!")


def re_mobile():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')

    setence = """
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    """

    mylist = re.findall(pattern, setence)
    print(mylist)
    print()

    for temp in pattern.finditer(setence):
        print(temp.group())
    print()

    m = pattern.search(setence)
    while m:
        print(m.group())
        m = pattern.search(setence, m.end())


def re_sensitive():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      "*", sentence, flags=re.I)

    print(purified)


def re_split():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'

    sentence_list = re.split(r'[，。,.]', poem)

    print(sentence_list)

    while '' in sentence_list:
        sentence_list.remove('')

    print(sentence_list)


if __name__ == '__main__':
    # re_qq()
    # re_mobile()
    # re_sensitive()
    re_split()
