# 在Python语言中，是天然支持装饰器的

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2016-12-04')
if  __name__=="__main__":
    now()
