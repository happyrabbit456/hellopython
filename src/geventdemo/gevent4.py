# 确定性
#
# greenlet具有确定性。在相同配置相同输入的情况下，它们总是会产生相同的输出。

import time

def echo(i):
    time.sleep(0.001)
    return i

if __name__ == "__main__":
    # Non Deterministic Process Pool
    from multiprocessing.pool import Pool

    p = Pool(10)
    run1 = [a for a in p.imap_unordered(echo, range(10))]
    run2 = [a for a in p.imap_unordered(echo, range(10))]
    run3 = [a for a in p.imap_unordered(echo, range(10))]
    run4 = [a for a in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)

    # Deterministic Gevent Pool
    from gevent.pool import Pool

    p = Pool(10)
    run1 = [a for a in p.imap_unordered(echo, range(10))]
    run2 = [a for a in p.imap_unordered(echo, range(10))]
    run3 = [a for a in p.imap_unordered(echo, range(10))]
    run4 = [a for a in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)
# 执行结果：
#
# False
# True
# 即使gevent通常带有确定性，当开始与如socket或文件等外部服务交互时， 不确定性也可能溜进你的程序中。因此尽管gevent线程是一种“确定的并发”形式， 使用它仍然可能会遇到像使用POSIX线程或进程时遇到的那些问题。
#
# 涉及并发长期存在的问题就是竞争条件(race condition)(当两个并发线程/进程都依赖于某个共享资源同时都尝试去修改它的时候， 就会出现竞争条件),这会导致资源修改的结果状态依赖于时间和执行顺序。 这个问题，会导致整个程序行为变得不确定。
#
# 解决办法: 始终避免所有全局的状态.
#
# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。