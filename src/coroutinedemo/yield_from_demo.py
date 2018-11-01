'''
从Python3.4开始asyncio模块加入到了标准库，通过asyncio我们可以轻松实现协程来完成异步IO操作。asyncio是一个基于事件循环的异步IO模块,通过yield from，我们可以将协程asyncio.sleep()的控制权交给事件循环，然后挂起当前协程；之后，由事件循环决定何时唤醒asyncio.sleep,接着向后执行代码。

下面这段代码，我们创造了一个协程display_date(num, loop)，然后它使用关键字yield from来等待协程asyncio.sleep(2)()的返回结果。而在这等待的2s之间它会让出CPU的执行权，直到asyncio.sleep(2)返回结果。asyncio.sleep(2)模拟的其实就是一个耗时2秒的IO读写操作。
'''


import asyncio
import datetime

@asyncio.coroutine  # 声明一个协程
def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果
loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()