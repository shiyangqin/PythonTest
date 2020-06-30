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
    p_list = [multiprocessing.Process(name="Process-" + str(i), target=func, args=(v, a)) for i in range(3)]
    [p.start() for p in p_list]
    [p.join() for p in p_list]
    print("-----------------------------------")
    print(v.value)
    print(a[:])


if __name__ == '__main__':
    value_demo()
