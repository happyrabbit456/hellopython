import os
import ctypes
import sys
from ctypes import *
import platform

sys.path.append('.')

CUR_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    print('starting...')

    a = ctypes.c_int(8)
    b = ctypes.c_int(9)
    a_ctypes_ptr = ctypes.byref(a)
    b_ctypes_ptr = ctypes.byref(b)

    # python调用vs2013  c + + Dll, 需要保持vs2013生成的调用约定一致，不能混用

    # stdcall调用约定：
    # dll = ctypes.WinDLL("PythonDll_stdcall")
    # dll = ctypes.WinDLL(os.path.join(CUR_PATH, 'PythonDll_stdcall'))
    dll = ctypes.windll.LoadLibrary("PythonDll_stdcall")
    print(dll.add(1,3))
    print(dll.sub(a_ctypes_ptr,b_ctypes_ptr))

    # cdecl调用约定：
    # lib = CDLL("PythonDll_cdecl.dll")
    lib = ctypes.cdll.LoadLibrary("PythonDll_cdecl.dll")
    print(lib.add(1,3))
    print(lib.sub(a_ctypes_ptr,b_ctypes_ptr))

    #  整数13是二进制的1101，所以应该输出3
    great_module = cdll.LoadLibrary('./great_module.dll')
    print(great_module.great_function(13))

    # 大家熟知的printf函数位于C标准库中。在C代码中调用printf是标准化的，但是，C标准库的实现不是标准化的。
    # 在Windows中，printf函数位于 %SystemRoot%\System32\msvcrt.dll，
    # 在Mac OS X中，它位于 /usr/lib/libc.dylib，
    # 在Linux中，一般位于 / usr/lib /libc.so.6
    cdll_names = {
        'Darwin': 'libc.dylib',
        'Linux': 'libc.so.6',
        'Windows': 'msvcrt.dll'
    }

    clib = cdll.LoadLibrary(cdll_names[platform.system()])
    # 函数原型int printf(const char * format, ...)
    clib.printf(c_char_p(b"Hello %d %f\n"), c_int(15), c_double(2.3))
    clib.printf(c_char_p("Hello %d %f\n".encode('utf-8')), c_int(15), c_double(2.3))

    # 如果不用构造函数，还可以用value成员。以下代码与
    # clib.printf(c_char_p("Hello %d %f"), c_int(15), c_double(2.3)) 等价：
    str_format = c_char_p()
    int_val = c_int()
    double_val = c_double()

    str_format.value = b"Hello %d %f\n"
    int_val.value = 15
    double_val.value = 2.3
    clib.printf(str_format, int_val, double_val)

    s1 = c_char_p(b'a')
    s2 = c_char_p(b'b')
    s3 = clib.strcat(s1, s2)
    print(s1.value)  # b'ab

    # 数组
    # 在C语言中，char是一种类型，char[100]是另外一种类型。
    # ctypes也是一样。使用数组需要预先生成需要的数组类型。
    type_int_array_10 = c_int * 10
    my_array = type_int_array_10()
    my_array[2] = c_int(5)
    print(great_module.array_get(my_array, 2))

    type_int_array_10 = c_int * 10
    type_int_array_10_10 = type_int_array_10 * 10
    my_array = type_int_array_10_10()
    my_array[1][2] = 3

    # 简单类型指针
    # 在ctypes中，指针类型用POINTER(ctypes_type)创建。
    # 例如创建一个类似于C语言的int *：
    type_p_int = POINTER(c_int)
    v = c_int(4)
    p_int = type_p_int(v)
    print(p_int[0])
    print(p_int.contents)

    type_p_int = POINTER(c_int)
    v = c_int(4)
    p_int = type_p_int(v)
    print(type(p_int))
    print(p_int[0])
    print(p_int.contents)
    # -------
    p_int = pointer(v)
    print(type(p_int))
    print(p_int[0])
    print(p_int.contents)

    # 函数指针
    # 它的函数原型是
    # void qsort(void * base, size_t num, size_t size, int (*compar)(const void *, const void *));
    CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

    def py_cmp_func(a, b):
        # print(type(a))
        # print("py_cmp_func", a[0], b[0])
        return a[0] - b[0]

    type_array_6 = c_int * 6
    ia = type_array_6(40, 10, 100, 90, 20, 25)
    clib.qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
    print(list(ia))


