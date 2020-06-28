# -*- coding:utf-8 -*-
import threading
import time


def run(t_name, sleep_time):
    print(t_name + " run")
    time.sleep(sleep_time)


def thread_demo_1():
    """线程创建示例1"""
    for i in range(5):
        t = threading.Thread(name="Thread-"+str(i), target=run, args=("Thread-"+str(i), i))
        print(t.getName() + " start")
        t.start()


class ThreadDemo2(threading.Thread):
    """Thread子类"""

    def run(self) -> None:
        print(self.getName() + " run")
        time.sleep(self._args[0])


def thread_demo_2():
    """线程创建示例2"""
    for i in range(5):
        t = ThreadDemo2(name="Thread-"+str(i), args=(i,))
        print(t.getName() + " start")
        t.start()


if __name__ == '__main__':
    # thread_demo_1()
    thread_demo_2()
