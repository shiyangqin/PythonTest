# -*- coding:utf-8 -*-
import multiprocessing


def func(v, a):
    while v.value < 5:
        v.value += 1
        print(v.value)
        for k, i in enumerate(a):
            a[k] = i + 1
        print(a[:])


def value_demo():
    v = multiprocessing.Value('d', 0)
    a = multiprocessing.Array('i', range(10))
    p1 = multiprocessing.Process(name="Process-1", target=func, args=(v, a))
    p2 = multiprocessing.Process(name="Process-2", target=func, args=(v, a))
    p3 = multiprocessing.Process(name="Process-3", target=func, args=(v, a))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("-----------------------------------")
    print(v.value)
    print(a[:])


if __name__ == '__main__':
    value_demo()
