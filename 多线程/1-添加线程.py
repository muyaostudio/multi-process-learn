#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1-添加线程.py
# @Author: muyao
# @Date  : 2020/2/6/006

import threading

import time


def thread_job1():
    print('T1 start\n')
    print('Fucking Thread %s' % threading.current_thread())
    for _ in range(5):
        time.sleep(0.1)
        print('T1 running')
    print('T1 finish\n')


def thread_job2():
    print('T2 start\n')
    print('Fucking Thread %s' % threading.current_thread())
    for _ in range(1):
        time.sleep(0.1)
        print('T2 running')
    print('T2 finish\n')


def main():
    added_thread1 = threading.Thread(target=thread_job1, name='T1byMuyaostudio')
    added_thread2 = threading.Thread(target=thread_job2, name='T2byMuyaostudio')

    added_thread1.start()
    added_thread2.start()

    added_thread1.join()  # 加上这行 T1运行完了才运行下面这些
    added_thread2.join()  # 加上这行 T2运行完了才运行下面这些

    print('激活了的线程数：', threading.active_count())  # 激活了的线程数
    print('查看已激活的线程：', threading.enumerate())  # 查看已激活的线程
    print('查看当前的线程：', threading.enumerate())  # 查看已激活的线程
    print('All done')


if __name__ == '__main__':
    main()
