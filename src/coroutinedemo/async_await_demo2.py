'''
asyncio的使用可分三步走：

创建事件循环
指定循环模式并运行
关闭循环
通常我们使用asyncio.get_event_loop()方法创建一个循环。

运行循环有两种方法：一是调用run_until_complete()方法，二是调用run_forever()方法。run_until_complete()内置add_done_callback回调函数，run_forever()则可以自定义add_done_callback()，具体差异请看下面两个例子。

使用run_until_complete()方法：
'''
import asyncio

async def func(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    print(loop.is_running())   # 查看当前状态时循环是否已经启动
    loop.run_until_complete(future)
    print(future.result())
    loop.close()