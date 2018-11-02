# Python与设计模式--迭代器模式


class Fibs:
    def __init__ (self):
        self.a =0
        self.b =1
    def __next__(self):
        self.a , self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self


if __name__=="__main__":
    lst=["hello Alice","hello Bob","hello Eve"]
    lst_iter=iter(lst)
    print(lst_iter)
    print(lst_iter.__next__())
    print(lst_iter.__next__())
    print(lst_iter.__next__())

    f=Fibs()
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())