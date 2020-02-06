#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: muyao
# @Date  : 2020/2/5/005
# 一个进程可以拥有多个线程
# 一个线程只能属于一个进程

import multiprocessing as mp


# import threading as td


def job(q, a, b):
    res = a + b
    q.put(res)
    # 不能写return 得把结果放进queue中


if __name__ == '__main__':
    # t1 = td.Thread(target=job, args=(1, 2))  # 创建一个线程

    q = mp.Queue()  # 进程运算完了放这里

    p1 = mp.Process(target=job, args=(q, 3, 4))  # 创建一个进程
    p2 = mp.Process(target=job, args=(q, 1, 2))  # args=(q,) 如果只有一个参数 这样写 说明其可迭代

    p1.start()  # 启动进程
    p2.start()

    p1.join()  # 实现进程间的同步，等待所有进程退出
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print(res1, res2)
