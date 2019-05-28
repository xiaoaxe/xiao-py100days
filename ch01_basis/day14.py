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

from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib.parse
import http.client
import json

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


def send_email():
    sender = 'xxxxxx@gmail.com'
    receivers = ['xxxxxx@qq.com']

    # 发送文本
    # message = MIMEText('用Python发送的邮件', 'plain', 'utf-8')
    # message['From'] = Header('小包', 'utf-8')
    # message['To'] = Header('dear', 'utf-8')
    # message['Subject'] = Header('示例代码实验邮件', 'utf-8')

    # 发送附件
    message = MIMEMultipart()
    text_content = MIMEText("附件中有数据", 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')

    # 添加文本正文
    message.attach(text_content)

    # 添加文本
    with open('/Users/baoqiang/1.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'

        message.attach(txt)

    # 添加xlxs
    with open('/Users/baoqiang/1.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=data.xlsx'

        message.attach(xls)

    smtper = SMTP('smtp.gmail.com', 587)
    # smtper = SMTP('smtp-relay.gmail.com', 587)
    smtper.ehlo()
    smtper.starttls()

    smtper.login(sender, 'xxxxxx')
    smtper.sendmail(sender, receivers, message.as_string())

    smtper.quit()

    print('send finish')


def send_request():
    """
    use requests is better
    :return:
    """

    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode(
        {'account': '你自己的账号', 'password': '你自己的密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号',
         'format': 'json'})
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    # clientit()
    # clientit2()
    send_email()
