# 除使用基本的Greenlet类之外，你也可以子类化Greenlet类，重载它的_run方法。

import gevent
from gevent import Greenlet

class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)

if __name__ == "__main__":
    g = MyGreenlet("Hi there!", 3)
    g.start()
    g.join()

# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。