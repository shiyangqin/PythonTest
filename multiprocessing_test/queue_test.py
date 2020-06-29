# -*- coding:utf-8 -*-
import multiprocessing
import time
import datetime


def put_process(queue):
    """添加元素进程"""
    print(datetime.datetime.now(), "start")
    for i in range(10):
        queue.put(i)
        time.sleep(1)


def get_process(queue):
    """消耗元素进程"""
    while True:
        value = queue.get()
        print(datetime.datetime.now(), value)
        if 9 <= value:
            print(datetime.datetime.now(), "end")
            break


def queue_demo():
    queue = multiprocessing.Queue()
    multiprocessing.Process(target=put_process, args=(queue,)).start()
    multiprocessing.Process(target=get_process, args=(queue,)).start()


if __name__ == '__main__':
    queue_demo()
