# -*- coding:utf-8 -*-
import multiprocessing
import time
import datetime


def left_process(left_pipe):
    """左通道进程"""
    print(datetime.datetime.now(), "start")
    left_pipe.send(1)
    while left_pipe.poll(2):
        value = left_pipe.recv()
        print(datetime.datetime.now(), "left_pipe recv:", value)
        if value < 10:
            time.sleep(1)
            left_pipe.send(value + 1)
        else:
            break


def right_process(right_pipe):
    """右通道进程"""
    while right_pipe.poll(2):
        value = right_pipe.recv()
        print(datetime.datetime.now(), "right_pipe recv:", value)
        time.sleep(1)
        right_pipe.send(value + 1)
    print(datetime.datetime.now(), "end")


def pipe_demo():
    left_pipe, right_pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=left_process, args=(left_pipe,))
    p2 = multiprocessing.Process(target=right_process, args=(right_pipe,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    left_pipe.close()
    right_pipe.close()


if __name__ == '__main__':
    pipe_demo()
