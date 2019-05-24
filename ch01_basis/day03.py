#!/usr/bin/env python
# encoding: utf-8

"""
@description: 条件语句

@author: baoqiang
@time: 2019-05-24 12:58
"""

import binascii


def fmt2():
    # a = -1.234
    a = 1.234
    print('{:+.2f}'.format(a))  # 保留符号，2位小数
    print('{:0>+10.2f}'.format(a))  # 靠右对齐，不足左边填充0，一共10位


def fmt():
    """
    10001
    21
    17
    11
    0x11
    0X11
    :return:
    """
    a = 17
    print('{:b}'.format(a))
    print('{:o}'.format(a))
    print('{:d}'.format(a))
    print('{:x}'.format(a))
    print('{:#x}'.format(a))
    print('{:#X}'.format(a))


def operator():
    """
    "unicode encode to bytes"
    :return:
    """

    flag = True

    if flag:
        # b'\xe4\xb8\xad\xe5\x9b\xbd'
        # \u4e2d\u56fd

        s4 = '中国'
        # print(s4.encode('utf-8'))
        # print(s4.encode('unicode-escape'))
        # print(s4.encode('utf-8').decode('ascii'))
        # print(s4.encode('unicode-escape').decode('ascii'))

        s5 = b'\xe4\xb8\xad\xe5\x9b\xbd'
        s6 = u'\u4e2d\u56fd'
        s7 = '\u4e2d\u56fd'
        print(s5.decode())
        print(s6)
        print(s7)

        s8 = '\xe4\xb8\xad\xe5\x9b\xbd'
        print(bytes(ord(i) for i in s8).decode())

        for i in s8:
            print(i)
            print(ord(i))

        s9 = '\\xe4\\xb8\\xad\\xe5\\x9b\\xbd'
        b9 = binascii.a2b_hex(s9.replace("\\x", ""))
        print(b9.decode())

    else:
        # 0b10001
        # 0o21
        # 0x11
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

        # print(int(f'{c2}', base=2))
        print(int('0b10001', base=2))
        print(bin(-6))

        f1 = 123.45
        f2 = 1.2345e2

        print(f1 == f2)

        s1 = "he\\llo"
        s2 = 'he\\llo'
        s3 = r'he\llo'

        print(s1 == s2)
        print(s1 == s3)

        b = b'\xe4\xb8\xad\xe6\x96\x87'

        print(b.decode())
        print(b.decode(encoding='utf-8'))

        # a=97 b=98
        b2 = b'\x61\x62'
        print(b2.decode())


if __name__ == '__main__':
    # operator()
    fmt2()
