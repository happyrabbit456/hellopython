# Gevent
#
# 介绍
#
# gevent是基于协程的Python网络库。特点：
#
# 基于libev的快速事件循环(Linux上epoll，FreeBSD上kqueue）。
# 基于greenlet的轻量级执行单元。
# API的概念和Python标准库一致(如事件，队列)。
# 可以配合socket，ssl模块使用。
# 能够使用标准库和第三方模块创建标准的阻塞套接字(gevent.monkey)。
# 默认通过线程池进行DNS查询,也可通过c-are(通过GEVENT_RESOLVER=ares环境变量开启）。
# TCP/UDP/HTTP服务器
# 子进程支持（通过gevent.subprocess）
# 线程池


# Greenlets
#
# gevent中的主要模式, 它是以C扩展模块形式接入Python的轻量级协程。 全部运行在主程序操作系统进程的内部，但它们被程序员协作式地调度。
#
# 在任何时刻，只有一个协程在运行。
# 区别于multiprocessing、threading等提供真正并行构造的库， 这些库轮转使用操作系统调度的进程和线程，是真正的并行。


# 同步和异步执行
#
# 并发的核心思想在于，大的任务可以分解成一系列的子任务，后者可以被调度成 同时执行或异步执行，而不是一次一个地或者同步地执行。两个子任务之间的 切换也就是上下文切换。
#
# 在gevent里面，上下文切换是通过yielding来完成的.

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
#
# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。