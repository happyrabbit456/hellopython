
def m2():
    f = open("output.txt", "w")
    try:
        f.write("python之禅")
    except IOError:
        print("oops error")
    finally:
        f.close()


# 一种更加简洁、优雅的方式就是用 with 关键字。
# open 方法的返回值赋值给变量 f，当离开 with 代码块的时候，
# 系统会自动调用 f.close() 方法，
# with 的作用和使用 try/finally 语句是一样的。
def m3():
    with open("output.txt", "w") as f:
        f.write("Python之禅")


class my_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


from contextlib import contextmanager
@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


if __name__=='__main__':
    m2()

    m3()

    with my_file('out.txt', 'w') as f:
        print("writing")
        f.write('hello, python')


    with my_open('out.txt', 'w') as f:
        f.write("hello , the simplest context manager")






