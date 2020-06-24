# -*- coding:utf-8 -*-
import threading


class ProblemDemo(object):
    """问题样例"""

    _item_list = ['item']

    @staticmethod
    def run():
        for i in range(100):
            threading.Thread(target=ProblemDemo.__process).start()

    @staticmethod
    def __process():
        for _ in range(10):
            print('remove item')
            ProblemDemo._item_list.remove('item')
            print('add item')
            ProblemDemo._item_list.append('item')


class LockDemo(object):
    """加锁样例"""

    _item_list = ['item']
    _item_list_lock = threading.Lock()

    @staticmethod
    def run():
        for i in range(100):
            threading.Thread(target=LockDemo.__process).start()

    @staticmethod
    def __process():
        for _ in range(10):
            with LockDemo._item_list_lock:
                print('remove item')
                LockDemo._item_list.remove('item')
                print('add item')
                LockDemo._item_list.append('item')


if __name__ == '__main__':
    # ProblemDemo.run()
    LockDemo.run()
