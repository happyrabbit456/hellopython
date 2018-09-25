# 2 可变参数
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)

# 3 关键字参数
def portrait(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k, v)

# 1 自调用
if __name__ == '__main__':
    print("__main__ done.")

    report('Mike', 8, 9)
    report('Mike', 8, 9, 10)

    portrait('Mike', age=24, country='China', education='bachelor')

    # copy =================================================
    # (1) id
    import copy
    a=[1,2,3]
    b=a
    print(id(a))
    print(id(b))
    print(id(a) == id(b))
    # result:
    # 2420476784200
    # 2420476784200
    # True
    # (2) 浅拷贝
    # 当使用浅拷贝时，python只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。
    import copy
    a=[1,2,3]
    c=copy.copy(a)
    print(id(a))
    print(id(c))
    print(id(a) == id(c))
    c[1]=2222
    print(a, c)
    # result:
    # 2420476784136
    # 2420476784008
    # False
    # [1, 2, 3][1, 2222, 3]
    # (3) 深拷贝
    # deepcopy对外围和内部元素都进行了拷贝对象本身，而不是对象的引用。
    import copy
    a = [1, 2, [3, 4]]  # 第三个值为列表[3,4],即内部元素
    # copy.copy()
    d = copy.copy(a)  # 浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身
    print(id(a) == id(d))
    print(id(a[2]) == id(d[2]))
    a[2][0] = 3333  # 改变a中内部原属列表中的第一个值
    print(a, d)  # 这时d中的列表元素也会被改变
    # copy.deepcopy()
    e = copy.deepcopy(a)  # e为深拷贝了a
    a[2][0] = 333  # 改变a中内部元素列表第一个的值
    print(a,e)
    # result:
    # False
    # True
    # [1, 2, [3333, 4]][1, 2, [3333, 4]]
    # 因为时深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变
    # [1, 2, [333, 4]][1, 2, [3333, 4]]
