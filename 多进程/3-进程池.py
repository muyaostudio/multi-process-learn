#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 3-进程池.py
# @Author: muyao
# @Date  : 2020/2/5/005

import multiprocessing as mp


def job(x):
    return x * x  # 在pool里可以有return


def multicore():
    pool = mp.Pool(processes=4)

    """apply方法是阻塞的:等待当前子进程执行完毕后，在执行下一个进程。"""
    res = pool.map(func=job, iterable=range(10))  # 把job和输入map一下
    print(res)

    """apply_async 是异步非阻塞的:不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。"""
    res = pool.apply_async(job, (2,))  # 只能输入一个值 若想输入多个值 看下面multi_Res
    print(res.get())

    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
