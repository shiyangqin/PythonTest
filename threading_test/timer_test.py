# -*- coding:utf-8 -*-
import datetime
import threading


def run(t_name):
    print(datetime.datetime.now(), " " + t_name + " run")


def timer_demo():
    """定时器创建示例"""
    for i in range(5):
        t = threading.Timer(interval=i, function=run, args=("timer-" + str(i),))
        t.start()


if __name__ == '__main__':
    timer_demo()
