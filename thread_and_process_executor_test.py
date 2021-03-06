# -*- coding:utf-8 -*-
import datetime
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def run(n):
    return str(datetime.datetime.now()) + ": " + str(n)


def thread_pool_executor_test():
    print(str(datetime.datetime.now()) + ": start")
    with ThreadPoolExecutor(2) as executor:
        f1 = executor.submit(run, 0)
        print(str(datetime.datetime.now()) + ": submit run")
        f2 = executor.map(run, (1, 2, 3))
        print(str(datetime.datetime.now()) + ": submit map")
    print(str(datetime.datetime.now()) + ": executor shutdown")
    print(type(f1))
    print(f1.result())

    print(type(f2))
    print(f2.__next__())
    print(f2.__next__())
    print(f2.__next__())


def process_pool_executor_test():
    print(str(datetime.datetime.now()) + ": start")
    executor = ProcessPoolExecutor(2)
    f1 = executor.submit(run, 0)
    print(str(datetime.datetime.now()) + ": submit run")
    f2 = executor.map(run, (1, 2, 3))
    print(str(datetime.datetime.now()) + ": submit map")
    print(type(f1))
    print(f1.result())

    print(type(f2))
    print(f2.__next__())
    print(f2.__next__())
    print(f2.__next__())
    executor.shutdown()
    print(str(datetime.datetime.now()) + ": executor shutdown")


if __name__ == '__main__':
    # thread_pool_executor_test()
    process_pool_executor_test()
