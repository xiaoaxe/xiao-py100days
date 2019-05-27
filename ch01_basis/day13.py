#!/usr/bin/env python
# encoding: utf-8

"""
@description: thread

@author: baoqiang
@time: 2019-05-25 22:36
"""

from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process, Queue
from threading import Thread, Lock
import tkinter
import tkinter.messagebox

"""
asyncio的异步代码
https://github.com/jackfrued/Python-100-Days/tree/master/Day01-15/Day13/code
"""


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())

    time_to_download = randint(2, 5)

    sleep(time_to_download)

    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


# 多进程下载
def process_download():
    start = time()

    p1 = Process(target=download_task, args=('book1',))
    p2 = Process(target=download_task, args=('book2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time()

    print("总共耗费了%.2f秒" % (end - start))


# 多进程下载
def thread_download():
    start = time()

    t1 = Thread(target=download_task, args=('book1',))
    t2 = Thread(target=download_task, args=('book2',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print("总共耗费了%.2f秒" % (end - start))


# 可以继承thread，并重写它的run方法
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


# 加锁
class Account:
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()

        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()
            # pass

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self) -> None:
        self._account.deposit(self._money)


def run_account():
    account = Account()
    threads = []

    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('账户余额为: ￥%d元' % account.balance)


def task_handler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)


def cal_num():
    processes = []

    number_list = [x for x in range(1, 10000001)]
    # number_list = [x for x in range(1, 10001)]
    result_queue = Queue()

    idx = 0
    for _ in range(8):
        next_idx = idx + int(len(number_list) / 8)
        p = Process(target=task_handler, args=(number_list[idx:next_idx], result_queue))

        idx += int(len(number_list) / 8)

        processes.append(p)

        p.start()

    start = time()

    for p in processes:
        p.join()

    total = 0

    while not result_queue.empty():
        total += result_queue.get()

    print("total: ", total)

    end = time()

    print('Execution time: ', (end - start), 's', sep='')


def async_gui():
    class DownloadTaskHandler(Thread):

        def run(self):
            sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    # process_download()
    # thread_download()
    # run_account()
    # cal_num()
    async_gui()
