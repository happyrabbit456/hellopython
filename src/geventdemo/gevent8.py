# 超时
#
# 通过超时可以对代码块儿或一个Greenlet的运行时间进行约束。

import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(10)

if __name__ == "__main__":
    try:
        gevent.spawn(wait).join()
    except Timeout:
        print('Could not complete')

# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。