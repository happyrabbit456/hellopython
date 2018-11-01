'''
最初的yield只能返回并暂停函数，并不能实现协程的功能。后来，Python为它定义了新的功能——接收外部发来的值，这样一个生成器就变成了协程。

每个生成器都可以执行send()方法，为生成器内部的yield语句发送数据。此时yield语句不再只是yield xxxx的形式，还可以是var = yield xxxx的赋值形式。它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数，并将这个值赋值给var变量！
'''


def simple_coroutine():
    print('-> 启动协程')
    y = 10
    x = yield y
    print('-> 协程接收到了x的值:', x)

my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(10)