# -*- coding:utf-8 -*-
import threading


class ProblemDemo(object):
    """死锁样例"""

    def __init__(self):
        self._item_1 = 0
        self._item_2 = 0
        self._item_1_lock = threading.Lock()
        self._item_2_lock = threading.Lock()

    def run(self):
        threading.Thread(target=self.__process_1).start()
        threading.Thread(target=self.__process_2).start()

    def __process_1(self):
        for _ in range(10):
            with self._item_1_lock:
                print("item_1 + 1")
                self._item_1 += 1
                with self._item_2_lock:
                    print("item_2 + 1")
                    self._item_2 += 1

    def __process_2(self):
        for _ in range(10):
            with self._item_2_lock:
                print("item_2 + 1")
                self._item_2 += 1
                with self._item_1_lock:
                    print("item_1 + 1")
                    self._item_1 += 1


class RLockDemo(object):
    """递归锁样例"""

    def __init__(self):
        self._item_1 = 0
        self._item_2 = 0
        self._item_1_lock = self._item_2_lock = threading.RLock()

    def run(self):
        threading.Thread(target=self.__process_1).start()
        threading.Thread(target=self.__process_2).start()

    def __process_1(self):
        for _ in range(10):
            with self._item_1_lock:
                print("item_1 + 1")
                self._item_1 += 1
                with self._item_2_lock:
                    print("item_2 + 1")
                    self._item_2 += 1

    def __process_2(self):
        for _ in range(10):
            with self._item_2_lock:
                print("item_2 + 1")
                self._item_2 += 1
                with self._item_1_lock:
                    print("item_1 + 1")
                    self._item_1 += 1


if __name__ == '__main__':
    # ProblemDemo().run()
    RLockDemo().run()
