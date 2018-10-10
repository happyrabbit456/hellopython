import sys
sys.path.append('.')

import lc_hello_world
print(dir(lc_hello_world))
print(lc_hello_world.test())
print(lc_hello_world.add(8, 2))

# print(lc_hello_world.add(1, '2'))  # 这个会报错

import test2
from test2 import *
print(test2.Add(1,2))
print(test2.Del(1,2))
a = World("abcdef")
print(a.greet())