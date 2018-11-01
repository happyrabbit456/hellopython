#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程/线程：操作系统提供的一种并发处理任务的能力。

协程：程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。

多进程和多线程体现的是操作系统的能力，而协程体现的是程序员的流程控制能力。看下面的例子，甲，乙两个工人模拟两个工作任务交替进行，在单线程内实现了类似多线程的功能。



最早的时候，Python提供了yield关键字，用于制造生成器。也就是说，包含有yield的函数，都是一个生成器！

yield的语法规则是：在yield这里暂停函数的执行，并返回yield后面表达式的值（默认为None），直到被next()方法再次调用时，从上次暂停的yield代码处继续往下执行。当没有可以继续next()的时候，抛出异常，该异常可被for循环处理。
'''

import time

def task1():
    while True:
        yield "<甲>也累了，让<乙>工作一会儿"
        time.sleep(1)
        print("<甲>工作了一段时间.....")


def task2(t):
    next(t)
    while True:
        print("-----------------------------------")
        print("<乙>工作了一段时间.....")
        time.sleep(2)
        print("<乙>累了，让<甲>工作一会儿....")
        ret = t.send(None)
        print(ret)
    t.close()

if __name__ == '__main__':
    t = task1()
    task2(t)