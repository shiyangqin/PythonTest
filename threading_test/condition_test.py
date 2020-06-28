# -*- coding:utf-8 -*-
import threading
from collections import deque


class ConditionDemo(object):
    """信号样例(参考Queue)"""

    def __init__(self, maxsize=0):
        """初始化队列"""
        self.maxsize = maxsize
        self._queue = deque()
        self.mutex = threading.Lock()
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)

    def size(self):
        """队列大小"""
        return len(self._queue)

    def is_full(self):
        """队列是否已满"""
        with self.mutex:
            return 0 < self.maxsize <= self.size()

    def is_empty(self):
        """队列是否已空"""
        with self.mutex:
            return not self.size()

    def put(self, item):
        """向队列中添加元素，队列满时挂起，调用get函数时唤醒"""
        print("put item")
        with self.not_full:
            if self.maxsize > 0:
                while self.size() >= self.maxsize:
                    print("put item wait")
                    self.not_full.wait()
            self._queue.append(item)
            self.not_empty.notify()

    def get(self):
        """从队列中获取元素，队列空时挂起，调用put函数时唤醒"""
        print("get item")
        with self.not_empty:
            while not self.size():
                print("get item wait")
                self.not_empty.wait()
            item = self._queue.popleft()
            self.not_full.notify()
            return item


if __name__ == '__main__':
    demo = ConditionDemo(1)
    print("size:" + str(demo.size()))
    print("is_empty:" + str(demo.is_empty()))
    print("is_full:" + str(demo.is_full()))

    threading.Timer(1, function=demo.put, args=(1,)).start()
    print(demo.get())

    threading.Timer(2, function=demo.get).start()
    demo.put(2)
    demo.put(3)

    print("size:" + str(demo.size()))
    print("is_empty:" + str(demo.is_empty()))
    print("is_full:" + str(demo.is_full()))
