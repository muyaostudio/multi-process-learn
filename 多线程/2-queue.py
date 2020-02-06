#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2-queue.py
# @Author: muyao
# @Date  : 2020/2/6/006

import threading
from queue import Queue


def job(l, q):
    # 对列表中每个值做计算
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


def multithreading(data):
    """
    多线程示例
    :param data: [[1,2,3],[3,4,5],[2,2,2],[5,5]] 
    :return: 
    """
    q = Queue()
    theads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        theads.append(t)

    # 让全部线程运行完
    for thead in theads:
        thead.join()

    # 把四组结果挨个拿出
    result = []
    for _ in range(4):
        result.append(q.get())
    print(result)


if __name__ == '__main__':
    data = [[1, 2, 3], [3, 4, 5], [2, 2, 2], [5, 5]]
    multithreading(data)
