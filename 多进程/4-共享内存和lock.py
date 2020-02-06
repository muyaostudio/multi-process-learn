#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 4-共享内存.py
# @Author: muyao
# @Date  : 2020/2/6/006
# shared memory

import multiprocessing as mp
import time

"""使用共享内存 让多核进行数据交流（全局变量行不通）"""
value = mp.Value('i', 1)  # 'i':int ,'d':double
array = mp.Array('i', [1, 2, 3])  # 1-dim


# print(value.value)
# print(list(array))


def job(v, num, l):
    l.acquire()  # 锁住
    for _ in range(10):
        time.sleep(0.1)
        v.value += num

        # p1 抢占进程
        if num == 1:
            print('p1抢占进程:', v.value)

        # p2 抢占进程
        if num == 3:
            print('p2抢占进程:', v.value)
    l.release()


def multicore():
    l = mp.Lock()  # 枷锁

    v = mp.Value('i', 0)  # i=0

    p1 = mp.Process(target=job, args=(v, 1, l))  # 创建一个进程
    p2 = mp.Process(target=job, args=(v, 3, l))  # args=(q,) 如果只有一个参数 这样写 说明其可迭代

    p1.start()  # 启动进程
    p2.start()

    p1.join()  # 实现进程间的同步，等待所有进程退出
    p2.join()


if __name__ == '__main__':
    multicore()
