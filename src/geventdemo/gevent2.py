# 网络延迟或IO阻塞隐式交出greenlet上下文的执行权。

import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    print('Started Polling: %s' % tic())
    select.select([], [], [], 1)
    print('Ended Polling: %s' % tic())

def gr2():
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
#
# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。