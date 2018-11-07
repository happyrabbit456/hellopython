# 猴子补丁(Monkey patching)

# gevent的死角.

import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)

# 执行结果：
#
# class 'socket.socket'
# After monkey patch
# class 'gevent.socket.socket'
#
# built-in function select
# After monkey patch
# function select at 0x1924de8
# Python的运行环境允许我们在运行时修改大部分的对象，包括模块，类甚至函数。 这是个一般说来令人惊奇的坏主意，因为它创造了“隐式的副作用”，如果出现问题 它很多时候是极难调试的。虽然如此，在极端情况下当一个库需要修改Python本身 的基础行为的时候，猴子补丁就派上用场了。在这种情况下，gevent能够修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行。
#
# 例如，Redis的python绑定一般使用常规的tcp socket来与redis-server实例通信。 通过简单地调用gevent.monkey.patch_all()，可以使得redis的绑定协作式的调度 请求，与gevent栈的其它部分一起工作。
#
# 这让我们可以将一般不能与gevent共同工作的库结合起来，而不用写哪怕一行代码。 虽然猴子补丁仍然是邪恶的(evil)，但在这种情况下它是“有用的邪恶(useful evil)”。

# 作者：softlns
# 链接：https://www.jianshu.com/p/c6053a4c3dd5
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。