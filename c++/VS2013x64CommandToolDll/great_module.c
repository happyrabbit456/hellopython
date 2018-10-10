//https://zhuanlan.zhihu.com/p/20152309

/*
Windows MSVC 下编译命令：（启动Visual Studio命令提示）

cl /LD great_module.c /o great_module.dll 

Windows GCC、Linux、Mac OS X下编译命令相同：

gcc -fPIC -shared -msse4.2 great_module.c -o great_module.dll
*/

//great_module.c
#include <nmmintrin.h>

#ifdef _MSC_VER
    #define DLL_EXPORT __declspec( dllexport ) 
#else
    #define DLL_EXPORT
#endif

//整数13是二进制的1101，所以应该输出3
DLL_EXPORT int great_function(unsigned int n) {
    return _mm_popcnt_u32(n);
}

//在C语言中，char 是一种类型，char [100]是另外一种类型。ctypes 也是一样。使用数组需要预先生成需要的数组类型。
DLL_EXPORT int array_get(int a[], int index) {
    return a[index];
}