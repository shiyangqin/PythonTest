# -*- coding:utf-8 -*-
import datetime
import threading


def run(t_name):
    print(datetime.datetime.now(), " " + t_name + " run")


def timer_demo1():
    """定时器创建示例1"""
    for i in range(5):
        t = threading.Timer(interval=i, function=run, args=("timer-" + str(i),))
        t.start()


class CallDemo(object):

    def __init__(self, t_name):
        self._t_name = t_name

    def __call__(self):
        self.run()

    def run(self):
        print(self._t_name + " run")


def timer_demo2():
    """定时器创建示例2"""
    for i in range(5):
        t = threading.Timer(interval=i, function=CallDemo("timer-" + str(i)))
        t.start()


if __name__ == '__main__':
    # timer_demo1()
    timer_demo2()
