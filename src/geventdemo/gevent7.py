# Greenlet状态
#
# greenlet的状态通常是一个依赖于时间的参数：
#
# started -- Boolean, 指示此Greenlet是否已经启动
# ready() -- Boolean, 指示此Greenlet是否已经停止
# successful() -- Boolean, 指示此Greenlet是否已经停止而且没抛异常
# value -- 任意值, 此Greenlet代码返回的值
# exception -- 异常, 此Greenlet内抛出的未捕获异常
# 程序停止
#
# 程序
# 当主程序(main program)收到一个SIGQUIT信号时，不能成功做yield操作的 Greenlet可能会令意外地挂起程序的执行。这导致了所谓的僵尸进程， 它需要在Python解释器之外被kill掉。
#
# 通用的处理模式就是在主程序中监听SIGQUIT信号，调用gevent.shutdown退出程序。





# 电脑系统是win10 64位，在使用python的signal模块时报错：“AttributeError: module 'signal' has no attribute 'SIGALRM'”，这是因为signal模块可以在linux下正常使用，但在windows下却有一些限制，在python文档https://docs.python.org/2/library/signal.html#signal.signal找到了如下解释：
#
# "On Windows, signal() can only be called with SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, or SIGTERM. A ValueError will be raised in any other case."
#
# 也就是说在windows下只能使用这几个信号：
#
# SIGABRT
# 	SIGFPE
# 	SIGILL
# 	SIGINT
# 	SIGSEGV
# 	SIGTERM

import gevent
import signal

def run_forever():
    gevent.sleep(1000)


def onsignal_term(a,b):
    print('收到SIGTERM信号')

if __name__ == '__main__':
    # gevent.signal(signal.SIGQUIT, gevent.shutdown)
    signal.signal(signal.SIGTERM, onsignal_term)

    thread = gevent.spawn(run_forever)
    thread.join()
#
# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。