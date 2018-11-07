# 同步vs异步

import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(5):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(5)]
    gevent.joinall(threads)



if __name__ == "__main__":
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()

# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。