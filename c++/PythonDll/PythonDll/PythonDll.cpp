// PythonDll.cpp : ���� DLL Ӧ�ó���ĵ���������
//

#include "stdafx.h"
#include "PythonDll.h"

#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

// ���ǵ���������һ��ʾ��
PYTHONDLL_API int nPythonDll=0;

// ���ǵ���������һ��ʾ����
PYTHONDLL_API int fnPythonDll(void)
{
	return 42;
}

// �����ѵ�����Ĺ��캯����
// �й��ඨ�����Ϣ������� PythonDll.h
CPythonDll::CPythonDll()
{
	return;
}

// Caijx added.
//ʹ��__stdcall���Ҽ�����->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, ��������Ϊ__stdcall���ɡ�
//ʹ��__cdecl���Ҽ�����->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, ��������Ϊ__cdecl���ɡ�
PYTHONDLL_API int add(int a, int b)
{
	int c = a + b;
	return c;
}

PYTHONDLL_API int sub(int *a, int *b)
{
	return *a - *b;
}
