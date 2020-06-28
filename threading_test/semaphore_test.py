# -*- coding:utf-8 -*-
import datetime
import threading
import time


class SemaphoreDemo(object):
    """Semaphore样例"""

    def __init__(self):
        self._sleep_time = 2
        self._available = threading.Semaphore(2)

    def run(self):
        for i in range(6):
            threading.Thread(target=self.__process).start()

    def __process(self):
        with self._available:
            print(datetime.datetime.now())
            time.sleep(self._sleep_time)
            self._available.release()


class BoundedSemaphoreDemo(object):
    """BoundedSemaphore样例"""

    def __init__(self):
        self._sleep_time = 2
        self._available = threading.BoundedSemaphore(2)

    def run(self):
        for i in range(6):
            threading.Thread(target=self.__process).start()

    def __process(self):
        with self._available:
            print(datetime.datetime.now())
            time.sleep(self._sleep_time)


if __name__ == '__main__':
    # SemaphoreDemo().run()
    BoundedSemaphoreDemo().run()
