# -*- coding:utf-8 -*-
import datetime
import threading


class EventDemo(object):
    """event样例"""

    def __init__(self):
        self._event_obj = threading.Event()

    def run(self):
        threading.Thread(target=self.__process_1).start()
        threading.Thread(target=self.__process_2).start()
        threading.Timer(2, function=self._event_obj.set).start()
        threading.Timer(4, function=self._event_obj.set).start()

    def __process_1(self):
        while not self._event_obj.is_set():
            print("process_1 wait")
            self._event_obj.wait()
        else:
            print("process_1:" + str(datetime.datetime.now()))
            self._event_obj.clear()

    def __process_2(self):
        while not self._event_obj.is_set():
            print("process_2 wait")
            self._event_obj.wait()
        else:
            self._event_obj.clear()
            print("process_2:" + str(datetime.datetime.now()))


if __name__ == '__main__':
    EventDemo().run()
