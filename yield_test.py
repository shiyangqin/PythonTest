# -*- coding:utf-8 -*-


def fibonacci(n):
    """生成器函数 - 斐波那契"""
    a, b, counter = 0, 1, 0
    while True:
        if n < counter:
            return
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == '__main__':
    f = fibonacci(10)
    try:
        while True:
            print(f.__next__())
    except StopIteration:
        pass
