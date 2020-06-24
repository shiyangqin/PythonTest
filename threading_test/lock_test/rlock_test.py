# -*- coding:utf-8 -*-
import threading


class ProblemDemo(object):
    """死锁样例"""

    _item_1 = 0
    _item_2 = 0
    _item_1_lock = threading.Lock()
    _item_2_lock = threading.Lock()

    @staticmethod
    def run():
        threading.Thread(target=ProblemDemo.__process_1).start()
        threading.Thread(target=ProblemDemo.__process_2).start()

    @staticmethod
    def __process_1():
        for _ in range(10):
            with ProblemDemo._item_1_lock:
                print("item_1 + 1")
                ProblemDemo._item_1 += 1
                with ProblemDemo._item_2_lock:
                    print("item_2 + 1")
                    ProblemDemo._item_2 += 1

    @staticmethod
    def __process_2():
        for _ in range(10):
            with ProblemDemo._item_2_lock:
                print("item_2 + 1")
                ProblemDemo._item_2 += 1
                with ProblemDemo._item_1_lock:
                    print("item_1 + 1")
                    ProblemDemo._item_1 += 1


class RLockDemo(object):
    """递归锁样例"""

    _item_1 = 0
    _item_2 = 0
    _item_1_lock = _item_2_lock = threading.RLock()

    @staticmethod
    def run():
        threading.Thread(target=RLockDemo.__process_1).start()
        threading.Thread(target=RLockDemo.__process_2).start()

    @staticmethod
    def __process_1():
        for _ in range(10):
            with RLockDemo._item_1_lock:
                print("item_1 + 1")
                RLockDemo._item_1 += 1
                with RLockDemo._item_2_lock:
                    print("item_2 + 1")
                    RLockDemo._item_2 += 1

    @staticmethod
    def __process_2():
        for _ in range(10):
            with RLockDemo._item_2_lock:
                print("item_2 + 1")
                RLockDemo._item_2 += 1
                with RLockDemo._item_1_lock:
                    print("item_1 + 1")
                    RLockDemo._item_1 += 1


if __name__ == '__main__':
    ProblemDemo.run()
    # RLockDemo.run()
