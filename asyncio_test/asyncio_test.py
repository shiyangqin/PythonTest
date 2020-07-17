# -*- coding:utf-8 -*-
import asyncio
import time


async def work(i, j):
    print('work-{}-{} start'.format(i, j))
    with open("{}.txt".format(str(time.time())), "a") as f:
        end_time = time.time() + 1
        while time.time() < end_time:
            f.write('work-{}-{}: {}'.format(i, j, time.time()))
    print('work-{}-{} end'.format(i, j))


async def test(n):
    print('test-{} start'.format(n))
    await asyncio.gather(
        work(n, 1),
        work(n, 2)
    )
    print('test-{} end'.format(n))
    return 0


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(i) for i in range(2)]))
    loop.close()
