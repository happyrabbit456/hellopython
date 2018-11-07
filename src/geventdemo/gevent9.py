# 超时类

# import gevent
# from gevent import Timeout
#
# time_to_wait = 5 # seconds
#
# class TooLong(Exception):
#     pass
#
# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)




# 另外，对各种Greenlet和数据结构相关的调用，gevent也提供了超时参数。

import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)

if __name__ == "__main__":
    timer = Timeout(1).start()
    thread1 = gevent.spawn(wait)

    try:
        thread1.join(timeout=timer)
    except Timeout:
        print('Thread 1 timed out')

    # --

    timer = Timeout.start_new(1)
    thread2 = gevent.spawn(wait)

    try:
        thread2.get(timeout=timer)
    except Timeout:
        print('Thread 2 timed out')

    # --

    try:
        gevent.with_timeout(1, wait)
    except Timeout:
        print('Thread 3 timed out')


# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。