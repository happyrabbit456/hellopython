# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但容易死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。

def coroutine(func):
    def ret():
        f = func()
        f.__next__()
        return f

    return ret


@coroutine
def consumer():
    print("Wait to getting a task")
    while True:
        n = (yield)
        print("Got %s", n)


import time


def producer():
    c = consumer()
    task_id = 0
    while True:
        time.sleep(1)
        print("Send a task %s to consumer" % task_id)
        c.send("task %s" % task_id)
        task_id=task_id+1


if __name__ == "__main__":
    producer()
#
# 作者：softlns
# 链接：https: // www.jianshu.com / p / c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。