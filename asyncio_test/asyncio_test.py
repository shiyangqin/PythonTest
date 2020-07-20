# -*- coding:utf-8 -*-
import asyncio
import time
import requests


async def work(i, j):
    print('work-{}-{} start'.format(i, j))
    end_time = time.time() + 1
    while time.time() < end_time:
        print('work-{}-{}: '.format(i, j) + requests.get("http://10.255.175.224/test").text)
    print('work-{}-{} end'.format(i, j))


async def test_1(n):
    print('test-{} start'.format(n))
    await asyncio.gather(work(n, 1), work(n, 2))
    print('test-{} end'.format(n))
    return 0


async def test_2(n):
    print('test-{} start'.format(n))
    f = asyncio.gather(work(n, 1), work(n, 2))
    print('test-{} end'.format(n))
    return 0


if __name__ == '__main__':
    asyncio.run(test_1(0))
    print("-----------------------------------")
    asyncio.run(test_2(1))
