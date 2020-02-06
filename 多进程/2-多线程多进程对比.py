#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2-多线程多进程对比.py
# @Author: muyao
# @Date  : 2020/2/5/005
# 剧透：多进程(core)完胜 多线程(thread)完败

import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += (i + i ** 2 + i ** 3)
    q.put(res)
    # 不能写return 得把结果放进queue中


"""Part 1 多进程"""
def multicore():
    # 多进程
    q = mp.Queue()  # 进程运算完了放这里

    p1 = mp.Process(target=job, args=(q,))  # 创建一个进程
    p2 = mp.Process(target=job, args=(q,))  # args=(q,) 如果只有一个参数 这样写 说明其可迭代

    p1.start()  # 启动进程
    p2.start()

    p1.join()  # 实现进程间的同步，等待所有进程退出
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print('MultiCore result = ', res1+res2)


"""Part 2 啥也不用"""
def normal():
    # 直接算 啥都不用
    res = 0
    for _ in range(2):
        # 为了控制变量 运行两次 因为进程线程都是2个
        for i in range(1000000):
            res += (i + i ** 2 + i ** 3)
    print('Normal result = ', res)


"""Part 3 多线程"""
def multithread():
    q = mp.Queue()  # 进程运算完了放这里

    t1 = td.Thread(target=job, args=(q,))  # 创建一个线程
    t2 = td.Thread(target=job, args=(q,))  # args=(q,) 如果只有一个参数 这样写 说明其可迭代

    t1.start()  # 启动进程
    t2.start()

    t1.join()  # 实现进程间的同步，等待所有进程退出
    t2.join()

    res1 = q.get()
    res2 = q.get()

    print('MultiThread result = ', res1+res2)


if __name__ == '__main__':

    # 啥都不用
    start_time = time.time()
    normal()
    end_time = time.time()
    print('Normal result = ', end_time - start_time)

    # 多线程
    start_time = time.time()
    multithread()
    end_time = time.time()
    print('MultiThread result = ', end_time - start_time)

    # 多进程(多核)
    start_time = time.time()
    multicore()
    end_time = time.time()
    print('MultiCore result = ', end_time - start_time)