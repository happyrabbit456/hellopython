import os
import ctypes
import sys
from ctypes import *

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