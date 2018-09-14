import threading

def f():
    print('Thread function\n')
    return


for i in range(3):
    t = threading.Thread(target=f)
    t.start()


class CustomThread(threading.Thread):
    def run(self):
        print('Custom thread function.\n')


for i in range(3):
    t = CustomThread()
    t.start()


import threading
import time


def f(i):
    for p in range(3):
        time.sleep(i + 1)
        print('Thread #', i, "\n")
        time.sleep(i)
    return


# start threads by passing function to Thread constructor
for i in range(3):
    t = threading.Thread(target=f, args=(i,))
    t.start()

# Result
#
# Thread # 0
#
# Thread # 1
#
# Thread # 0
#
# Thread # 0
#
# Thread # 2
#
# Thread # 1
#
# Thread # 1
#
# Thread # 2
#
# Thread # 2


import threading
import time


def f(i):
    time.sleep(i)
    return


# threads
t1 = threading.Thread(target=f, args=(1.2,), name="Thread#1")
t1.start()

t2 = threading.Thread(target=f, args=(2.2,), name="Thread#2")
t2.start()

for p in range(5):
    time.sleep(p * 0.5)
    print('[', time.ctime(), ']', t1.getName(), t1.is_alive())
    print('[', time.ctime(), ']', t2.getName(), t2.is_alive())

# Result
#
# [ Tue Feb 27 17:58:54 2018 ] Thread#1 True
# [ Tue Feb 27 17:58:54 2018 ] Thread#2 True
# [ Tue Feb 27 17:58:55 2018 ] Thread#1 True
# [ Tue Feb 27 17:58:55 2018 ] Thread#2 True
# [ Tue Feb 27 17:58:56 2018 ] Thread#1 False
# [ Tue Feb 27 17:58:56 2018 ] Thread#2 True
# [ Tue Feb 27 17:58:57 2018 ] Thread#1 False
# [ Tue Feb 27 17:58:57 2018 ] Thread#2 False
# [ Tue Feb 27 17:58:59 2018 ] Thread#1 False
# [ Tue Feb 27 17:58:59 2018 ] Thread#2 False


import threading
import time


def f(i):
    for p in range(3):
        time.sleep(i + 1.5)
        print(threading.current_thread().getName())
    return


# start threads by passing function to Thread constructor
for i in range(3):
    t = threading.Thread(target=f, args=(i,))
    t.setName('Thread#' + str(i))
    t.start()

# Result
# Thread#0
# Thread#1
# Thread#0
# Thread#2
# Thread#0
# Thread#1
# Thread#2
# Thread#1
# Thread#2