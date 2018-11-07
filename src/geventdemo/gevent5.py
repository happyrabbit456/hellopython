# 创建Greenlets
#
# gevent对Greenlet初始化提供了一些封装.

import gevent
from gevent import Greenlet

def foo(message, n):
    gevent.sleep(n)
    print(message)

if __name__ == "__main__":
    thread1 = Greenlet.spawn(foo, "Hello", 1)
    thread2 = gevent.spawn(foo, "I live!", 2)
    thread3 = gevent.spawn(print(list(map(lambda x:x*x,range(1,5)))))
    threads = [thread1, thread2, thread3]
    gevent.joinall(threads)
# 执行结果：
#
# Hello
# I live!
#
# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。