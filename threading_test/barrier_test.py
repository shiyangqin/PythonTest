# -*- coding:utf-8 -*-
import threading
import time
import datetime


class BarrierDemo(object):
    """barrier样例"""

    def __init__(self):
        self._barrier_obj = threading.Barrier(2)

    def run(self):
        print(datetime.datetime.now())
        for i in range(5):
            threading.Thread(target=self.__process, args=(i,)).start()

    def __process(self, sleep_time):
        time.sleep(sleep_time)
        try:
            self._barrier_obj.wait(2)
        except RuntimeError:
            print('error')
        print(datetime.datetime.now())


if __name__ == '__main__':
    BarrierDemo().run()
