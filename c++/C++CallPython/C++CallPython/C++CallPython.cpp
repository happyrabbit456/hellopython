// C++CallPython.cpp : �������̨Ӧ�ó������ڵ㡣
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
	Py_Initialize();  //����Py_Initialize()���г�ʼ��
	if (!Py_IsInitialized())
		return -1;

	PyRun_SimpleString("print('Hello World!!')");

	PyRun_SimpleString("import sys; sys.path.append('.')");
	PyRun_SimpleString("import mytest;");
	PyRun_SimpleString("print(mytest.myabs(-2.0))");
	
	Py_Finalize(); //����Py_Finalize,��Py_Initialize���Ӧ��.


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

	//C++��Ƕ��python���򡪡�������ģʽ
	system("python hello.py");

	system("pause");

	return 0;
}

//�������"Hello World"����  
void HelloWorld()
{
	Py_Initialize(); //ʹ��python֮ǰ��Ҫ����Py_Initialize();����������г�ʼ��  
	if (!Py_IsInitialized())
	{
		cout << "Py_Initialize call error" << endl;
		return;
	}
	
	PyObject * pModule = NULL;    //��������  
	PyObject * pFunc = NULL;      //��������  
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");              //������Ҫ���õ�Python�ļ���  
	if (pModule!=NULL)
	{
		pFunc = PyObject_GetAttrString(pModule, "helloworld");   //������Ҫ���õĺ�����  
		if (pFunc!=NULL)
		{
			PyEval_CallObject(pFunc, NULL);                         //���ú���,NULL��ʾ����Ϊ��  
		}
	}	
	Py_Finalize();                //����Py_Finalize,�����Py_Initialize���Ӧ��.  
}

//����Add����,������int�Ͳ���  
void Add()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python�ļ���  
	if (pModule){
		pFunc = PyObject_GetAttrString(pModule, "add");  //Add:Python�ļ��еĺ�����  
		if (pFunc){
			//��������:  
			PyObject *pArgs = PyTuple_New(2);               //�������õĲ������ݾ�����Ԫ�����ʽ�����,2��ʾ��������  
			PyTuple_SetItem(pArgs, 0, Py_BuildValue("i", 5));//0---���  i��ʾ����int�ͱ���  
			PyTuple_SetItem(pArgs, 1, Py_BuildValue("i", 7));//1---���  
			//����ֵ  
			PyObject *pReturn = NULL;
			pReturn = PyEval_CallObject(pFunc, pArgs);      //���ú���  
			//������ֵת��Ϊint����  
			int result;
			PyArg_Parse(pReturn, "i", &result);    //i��ʾת����int�ͱ���  
			cout << "5+7 = " << result << endl;
		}		
	}

	Py_Finalize();
}

//�������ݵ�����Ϊ�ֵ�  
void TestTransferDict()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python�ļ��� 
	if (pModule){
		pFunc = PyObject_GetAttrString(pModule, "testdict"); //Add:Python�ļ��еĺ�����  
		if (pFunc){
			//��������:  
			PyObject *pArgs = PyTuple_New(1);
			PyObject *pDict = PyDict_New();   //�����ֵ����ͱ���  
			PyDict_SetItemString(pDict, "Name", Py_BuildValue("s", "WangYao")); //���ֵ����ͱ������������  
			PyDict_SetItemString(pDict, "Age", Py_BuildValue("i", 25));         //���ֵ����ͱ������������  
			PyTuple_SetItem(pArgs, 0, pDict);//0---���  ���ֵ����ͱ�����ӵ�����Ԫ����  
			//����ֵ  
			PyObject *pReturn = NULL;
			pReturn = PyEval_CallObject(pFunc, pArgs);      //���ú���  
			//������ֵ: 
			Py_ssize_t retSize = PyDict_Size(pReturn);
			int size = static_cast<int>(retSize);
			cout << "�����ֵ�Ĵ�СΪ: " << size << endl;
			PyObject *pNewAge = PyDict_GetItemString(pReturn, "Age");
			int newAge;
			PyArg_Parse(pNewAge, "i", &newAge);
			cout << "True Age: " << newAge << endl;
		}
	}	

	Py_Finalize();
}

//������  
void TestClass()
{
	Py_Initialize();
	if (!Py_IsInitialized())
		return;

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	PyObject * pDict = NULL;
	PyRun_SimpleString("import sys; sys.path.append('.')");
	pModule = PyImport_ImportModule("test001");      //test001:Python�ļ���  
	if (pModule){
		pDict = PyModule_GetDict(pModule);
		if (pDict){
			//��ȡPerson�� 
			PyObject * pClassPerson = PyDict_GetItemString(pDict, "Person");
			if (pClassPerson){
				//����Person���ʵ��  
				//PyObject *pInstancePerson = PyInstance_New(pClassPerson, NULL, NULL);//Python2.7�иýӿڣ�Python3.5û�иýӿڡ�	
				PyObject *pInstancePerson = PyInstanceMethod_New(pClassPerson);
				if (pInstancePerson){	
					//���÷���  
					PyObject_CallMethod(pInstancePerson, "greet", "(s, s)", "", "Hello Kitty");   //s��ʾ���ݵ����ַ���,ֵΪ"Hello Kitty" 
					PyObject_CallMethod(pInstancePerson, "greet", "s:s", "", "Hello Cai");   //s��ʾ���ݵ����ַ���,ֵΪ"Hello Cai" 
					
					//������ķ���
					PyObject *result = PyObject_CallMethod(pInstancePerson, "say_hello", "(s,s)", "", "charity");

					//�������ֵ	
					char* name = NULL;	
					PyArg_Parse(result, "s", &name);   //��������ĵڶ�������������ʹ���ַ�����ʾ�ģ����硰s������ str "i" ����int	
					printf("%s\n", name);										
				}
			}
		}
	}	
	
	Py_Finalize();
}

