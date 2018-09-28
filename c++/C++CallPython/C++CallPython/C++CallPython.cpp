// C++CallPython.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdlib>

#include <Python.h>

using namespace std;

void HelloWorld();
void Add();
void TestTransferDict();
void TestClass();

int _tmain(int argc, _TCHAR* argv[])
{
	Py_Initialize();  //调用Py_Initialize()进行初始化
	if (!Py_IsInitialized())
		return -1;

	PyRun_SimpleString("print('Hello World!!')");

	PyRun_SimpleString("import sys; sys.path.append('.')");
	PyRun_SimpleString("import mytest;");
	PyRun_SimpleString("print(mytest.myabs(-2.0))");
	
	Py_Finalize(); //调用Py_Finalize,和Py_Initialize相对应的.


	cout << "Starting Test..." << endl;

	cout << "helloworld()-------------" << endl;
	HelloWorld();
	cout << "Add()--------------------" << endl;
	Add();
	cout << "TestDict-----------------" << endl;
	TestTransferDict();
	cout << "TestClass----------------" << endl;
	TestClass();

	cout << "Ending Test..." << endl;

	//C++中嵌入python程序——命令行模式
	system("python hello.py");

	system("pause");

	return 0;
}

//调用输出"Hello World"函数  
void HelloWorld()
{
	Py_Initialize(); //使用python之前，要调用Py_Initialize();这个函数进行初始化  
	if (!Py_IsInitialized())
	{
		cout << "Py_Initialize call error" << endl;
		return;
	}
	
	PyObject * pModule = NULL;    //声明变量  
	PyObject * pFunc = NULL;      //声明变量  
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");              //这里是要调用的Python文件名  
	if (pModule!=NULL)
	{
		pFunc = PyObject_GetAttrString(pModule, "helloworld");   //这里是要调用的函数名  
		if (pFunc!=NULL)
		{
			PyEval_CallObject(pFunc, NULL);                         //调用函数,NULL表示参数为空  
		}
	}	
	Py_Finalize();                //调用Py_Finalize,这个和Py_Initialize相对应的.  
}

//调用Add函数,传两个int型参数  
void Add()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python文件名  
	if (pModule){
		pFunc = PyObject_GetAttrString(pModule, "add");  //Add:Python文件中的函数名  
		if (pFunc){
			//创建参数:  
			PyObject *pArgs = PyTuple_New(2);               //函数调用的参数传递均是以元组的形式打包的,2表示参数个数  
			PyTuple_SetItem(pArgs, 0, Py_BuildValue("i", 5));//0---序号  i表示创建int型变量  
			PyTuple_SetItem(pArgs, 1, Py_BuildValue("i", 7));//1---序号  
			//返回值  
			PyObject *pReturn = NULL;
			pReturn = PyEval_CallObject(pFunc, pArgs);      //调用函数  
			//将返回值转换为int类型  
			int result;
			PyArg_Parse(pReturn, "i", &result);    //i表示转换成int型变量  
			cout << "5+7 = " << result << endl;
		}		
	}

	Py_Finalize();
}

//参数传递的类型为字典  
void TestTransferDict()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python文件名 
	if (pModule){
		pFunc = PyObject_GetAttrString(pModule, "testdict"); //Add:Python文件中的函数名  
		if (pFunc){
			//创建参数:  
			PyObject *pArgs = PyTuple_New(1);
			PyObject *pDict = PyDict_New();   //创建字典类型变量  
			PyDict_SetItemString(pDict, "Name", Py_BuildValue("s", "WangYao")); //往字典类型变量中填充数据  
			PyDict_SetItemString(pDict, "Age", Py_BuildValue("i", 25));         //往字典类型变量中填充数据  
			PyTuple_SetItem(pArgs, 0, pDict);//0---序号  将字典类型变量添加到参数元组中  
			//返回值  
			PyObject *pReturn = NULL;
			pReturn = PyEval_CallObject(pFunc, pArgs);      //调用函数  
			//处理返回值: 
			Py_ssize_t retSize = PyDict_Size(pReturn);
			int size = static_cast<int>(retSize);
			cout << "返回字典的大小为: " << size << endl;
			PyObject *pNewAge = PyDict_GetItemString(pReturn, "Age");
			int newAge;
			PyArg_Parse(pNewAge, "i", &newAge);
			cout << "True Age: " << newAge << endl;
		}
	}	

	Py_Finalize();
}

//测试类  
void TestClass()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyObject * pDict = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python文件名  
	if (pModule){
		pDict = PyModule_GetDict(pModule);
		if (pDict){
			//获取Person类 
			PyObject * pClassPerson = PyDict_GetItemString(pDict, "Person");
			if (pClassPerson){
				//创建Person类的实例  
				//PyObject *pInstancePerson = PyInstance_New(pClassPerson, NULL, NULL);//Python2.7有该接口，Python3.5没有该接口。	
				PyObject *pInstancePerson = PyInstanceMethod_New(pClassPerson);
				if (pInstancePerson){	
					//调用方法  
					PyObject_CallMethod(pInstancePerson, "greet", "(s, s)", "", "Hello Kitty");   //s表示传递的是字符串,值为"Hello Kitty" 
					PyObject_CallMethod(pInstancePerson, "greet", "s:s", "", "Hello Cai");   //s表示传递的是字符串,值为"Hello Cai" 
					
					//调用类的方法
					PyObject *result = PyObject_CallMethod(pInstancePerson, "say_hello", "(s,s)", "", "charity");

					//输出返回值	
					char* name = NULL;	
					PyArg_Parse(result, "s", &name);   //这个函数的第二个参数，类型使用字符来表示的，例如“s”代表 str "i" 代表int	
					printf("%s\n", name);										
				}
			}
		}
	}	
	
	Py_Finalize();
}

