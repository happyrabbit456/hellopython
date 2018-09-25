import multiprocessing as mp
import threading as td

# 添加进程Process和Thread

def job_0(a,d):
    print('aaaaa')


# 存储进程输出Queue
def job_1(q):
    res = 0
    for i in range(100):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue


# 4 效率对比threading&multiprocessing
# 上篇讲了多进程/多核的运算，这次我们来对比下多进程，多线程和什么都不做时的消耗时间，看看哪种方式更有效率。
# （1）创建多进程 multiprocessing
# 和上节一样，首先import multiprocessing并定义要实现的job()，同时为了容易比较，我们将计算的次数增加到1000000
import multiprocessing as mp
def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue
# 因为多进程是多核运算，所以我们将上节的多进程代码命名为multicore()
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)
# （2）创建多线程 multithread
# 接下来创建多线程程序，创建多线程和多进程有很多相似的地方。首先import threading然后定义multithread()完成同样的任务
import threading as td
def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
# （3）创建普通函数
# 最后我们定义最普通的函数。注意，在上面例子中我们建立了两个进程或线程，均对job()进行了两次运算，所以在normal()中我们也让它循环两次
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)

# 进程池Pool
def job_2(x):
    return x*x

def multicore_1():
    pool = mp.Pool()
    res = pool.map(job_2, range(10))
    print(res)
    res = pool.apply_async(job_2, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job_2, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])

# 进程锁Lock
import multiprocessing as mp
import time
def job_3(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

def multicore_2():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job_3, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job_3, args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=='__main__':
    # 添加进程Process和Thread
    t1 = td.Thread(target=job_0, args=(1, 2))
    p1 = mp.Process(target=job_0, args=(1, 2))
    t1.start()
    p1.start()
    t1.join()
    p1.join()

    # 存储进程输出Queue
    q = mp.Queue()
    p1 = mp.Process(target=job_1, args=(q,))  # 注意args如果只有一个参数，要在后边加上逗号,
    p2 = mp.Process(target=job_1, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)

    # 对比各函数运行时间 ==>> 多进程<普通<多线程
    import time
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)

    # 进程池Pool
    multicore_1()

    # 进程锁Lock
    multicore_2()