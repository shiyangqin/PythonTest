# -*- coding:utf-8 -*-
import threading


class ProblemDemo(object):
    """问题样例"""

    def __init__(self):
        self._item_list = ['item']

    def run(self):
        for i in range(100):
            threading.Thread(target=self.__process).start()

    def __process(self):
        for _ in range(10):
            print('remove item')
            self._item_list.remove('item')
            print('add item')
            self._item_list.append('item')


class LockDemo(object):
    """加锁样例"""

    def __init__(self):
        self._item_list = ['item']
        self._item_list_lock = threading.Lock()

    def run(self):
        for i in range(100):
            threading.Thread(target=self.__process).start()

    def __process(self):
        for _ in range(10):
            with self._item_list_lock:
                print('remove item')
                self._item_list.remove('item')
                print('add item')
                self._item_list.append('item')


if __name__ == '__main__':
    # ProblemDemo().run()
    LockDemo().run()
