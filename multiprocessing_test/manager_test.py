# -*- coding:utf-8 -*-
import multiprocessing


def func(arr, l_lock):
    for _ in range(100):
        with l_lock:
            print('remove item')
            arr.remove('item')
            print('add item')
            arr.append('item')


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    l_list = manager.list()
    l_list.append('item')
    l_list_lock = manager.Lock()
    # p_list = [multiprocessing.Process(target=func, args=(l_list, l_list_lock)) for _ in range(3)]
    # [i.start() for i in p_list]
    # [i.join() for i in p_list]
    pool = multiprocessing.pool.Pool(3)
    pool.starmap_async(func, ((l_list, l_list_lock),))
    pool.starmap_async(func, ((l_list, l_list_lock),))
    pool.starmap_async(func, ((l_list, l_list_lock),))
    pool.close()
    pool.join()
