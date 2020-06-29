# -*- coding:utf-8 -*-
import multiprocessing
import time


def run(t_name, sleep_time):
    print(t_name + " run")
    time.sleep(sleep_time)


def process_demo_1():
    """进程创建示例1"""
    for i in range(5):
        p = multiprocessing.Process(name="Process-"+str(i), target=run, args=("Process-"+str(i), i))
        print(p.name + " start")
        p.start()


class ProcessDemo2(multiprocessing.Process):
    """Process子类"""

    def run(self) -> None:
        print(self.name + " run")
        time.sleep(self._args[0])


def process_demo_2():
    """进程创建示例2"""
    for i in range(5):
        p = ProcessDemo2(name="Process-"+str(i), args=(i,))
        print(p.name + " start")
        p.start()


class CallDemo(object):

    def __init__(self, t_name, sleep_time):
        self._t_name = t_name
        self._sleep_time = sleep_time

    def __call__(self):
        self.run()

    def run(self):
        print(self._t_name + " run")
        time.sleep(self._sleep_time)


def process_demo_3():
    """进程创建示例3"""
    for i in range(5):
        p = multiprocessing.Process(name="Process-"+str(i), target=CallDemo("Process-"+str(i), i))
        print(p.name + " start")
        p.start()


class DaemonDemo(multiprocessing.Process):
    """守护进程样例"""

    def run(self) -> None:
        print(self.name + " run")
        time.sleep(self._args[0])
        print(self.name + " end")


def daemon_demo():
    """守护进程样例"""
    p = DaemonDemo(name="Process-daemon", args=(2,), daemon=True)
    print(p.name + " start")
    p.start()
    time.sleep(1)


if __name__ == '__main__':
    # process_demo_1()
    # process_demo_2()
    # process_demo_3()
    daemon_demo()
