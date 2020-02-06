#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 3-lcok.py
# @Author: muyao
# @Date  : 2020/2/6/006

import threading


def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1: A =', A)
    lock.release()


def job2():
    global A, lock
    with lock:
        for i in range(10):
            A *= 10
            print('job2: A =', A)


if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('final: A =', A)
