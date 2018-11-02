"""
享元模式
使用共享技术支持大量细粒度的对象
使用几种对象就可以表示所有的对象
应用场景：对象的结构基本相同，但需要生成大量的对象
"""
from abc import ABCMeta, abstractmethod


class Go(object):
    """
    围棋棋子抽象基类
    """
    __metaclass__ = ABCMeta

    def __init__(self, color):
        self.color = color
        pass

    @abstractmethod
    def play(self, position):
        pass


class ConcreteGo(Go):
    def __init__(self, color):
        super(ConcreteGo, self).__init__(color)

    def play(self, position):
        print(self.color + "下在" + str(position) + "上")


class Factory(object):
    def __init__(self):
        self._go_dict = dict()
        pass

    def create_go(self, color):
        if color in self._go_dict:
            return self._go_dict[color]
        else:
            self._go_dict[color] = ConcreteGo(color)
            return self._go_dict[color]

    def count(self):
        print("一共有{0}种棋子，分别是：".format(len(self._go_dict)))
        for k, v in enumerate(self._go_dict):
            print(v)


if __name__ == '__main__':
    factory = Factory()
    white1 = factory.create_go("白棋")
    white1.play(1)
    black1 = factory.create_go("黑棋")
    black1.play(2)
    white2 = factory.create_go("白棋")
    white3 = factory.create_go("白棋")
    white4 = factory.create_go("白棋")
    white2.play(3)
    white3.play(4)
    white4.play(5)

    print("")
    factory.count()
# ---------------------
# 作者：拖油瓶ZZH
# 来源：CSDN
# 原文：https://blog.csdn.net/a23764996/article/details/54347872
# 版权声明：本文为博主原创文章，转载请附上博文链接！