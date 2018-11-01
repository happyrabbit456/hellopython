'''
yield的语法规则是：在yield这里暂停函数的执行，并返回yield后面表达式的值（默认为None），直到被next()方法再次调用时，从上次暂停的yield代码处继续往下执行。当没有可以继续next()的时候，抛出异常，该异常可被for循环处理。
'''

# 下面是通过for循环不断地使fib生成下一个数，实际上就是不断地调用next()方法。

def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a+b
        i += 1

if __name__ == '__main__':
    f = fib(10)
    for item in f:
        print(item)