// PythonDll.cpp : 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#include "PythonDll.h"

#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

// 这是导出变量的一个示例
PYTHONDLL_API int nPythonDll=0;

// 这是导出函数的一个示例。
PYTHONDLL_API int fnPythonDll(void)
{
	return 42;
}

// 这是已导出类的构造函数。
// 有关类定义的信息，请参阅 PythonDll.h
CPythonDll::CPythonDll()
{
	return;
}

// Caijx added.
//使用__stdcall，右键工程->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, 将其设置为__stdcall即可。
//使用__cdecl，右键工程->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, 将其设置为__cdecl即可。
PYTHONDLL_API int add(int a, int b)
{
	int c = a + b;
	return c;
}

PYTHONDLL_API int sub(int *a, int *b)
{
	return *a - *b;
}
