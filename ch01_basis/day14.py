#!/usr/bin/env python
# encoding: utf-8

"""
@description: network

@author: baoqiang
@time: 2019-05-25 22:36
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
import json
from threading import Thread
import base64

"""
七层网络模型：
应用层，表示层，会话层
传输层
网络层
数据链路层，物理层

四层模型
应用层
传输层
网络层
网络接口层

nat网络地址转换：局域网和公网ip一一对应的技术
"""


def serverit():
    """
    ('127.0.0.1', 50051) connected
    :return:
    """

    # SOCK_STREAM=tcp SOCK_DGRAM=udp
    server = socket(family=AF_INET, type=SOCK_STREAM)

    server.bind(("127.0.0.1", 4321))

    # queue size
    server.listen(512)

    while True:
        client, addr = server.accept()

        print('{} connected'.format(addr))

        client.send('{}'.format(datetime.now()).encode('utf-8'))

        client.close()


def serverit2():
    """
    :return:
    """

    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self) -> None:
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            my_dict['filedata'] = data

            json_str = json.dumps(my_dict)

            self.cclient.send(json_str.encode())

            self.cclient.close()

    # SOCK_STREAM=tcp SOCK_DGRAM=udp
    server = socket(family=AF_INET, type=SOCK_STREAM)

    server.bind(("127.0.0.1", 4321))

    # queue size
    server.listen(512)

    with open('guido.jpg', 'rb') as f:
        raw_data = f.read()
        data = base64.b64encode(raw_data).decode()

    while True:
        client, addr = server.accept()

        print('{} connected'.format(addr))

        FileTransferHandler(client).start()

        client.close()


def clientit():
    """
    received: 2019-05-28 14:37:07.234834
    :return:
    """

    client = socket()
    client.connect(('127.0.0.1', 4321))

    data = client.recv(4096).decode('utf-8')

    print('received: {}'.format(data))

    client.close()


def clientit2():
    """
    :return:
    """

    client = socket()
    client.connect(('127.0.0.1', 4321))

    in_datas = bytes()

    # receive batch
    data = client.recv(4096)

    while data:
        in_datas += data
        data = client.recv(4096)

    my_dict = json.loads(in_datas.decode())

    filename = 'new_{}'.format(my_dict['filename'])
    filedata = my_dict['filedata'].encode()

    with open(filename, 'wb') as fw:
        fw.write(base64.b64decode(filedata))

    client.close()


def print_color():
    pass


if __name__ == '__main__':
    # clientit()
    clientit2()
