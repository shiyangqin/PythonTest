# -*- coding:utf-8 -*-
import multiprocessing
import os


def run(i):
    print(i+2)
    return i+2


def pool_demo():
    pool = multiprocessing.Pool(os.cpu_count() or 3)
    a1 = pool.apply_async(run, (1,))
    a2 = pool.apply_async(run, (2,))
    m = pool.map_async(run, [1, 2])
    s = pool.starmap_async(run, [(1,), (2,)])
    print("a1:", a1.ready())
    pool.close()
    pool.join()
    print("a1:", a1.successful())
    print("a1:", a1.get())
    print("a2:", a2.get())
    print("m:", m.get())
    print("s:", s.get())


if __name__ == '__main__':
    pool_demo()
