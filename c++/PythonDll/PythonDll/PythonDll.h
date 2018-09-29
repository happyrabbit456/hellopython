// 下列 ifdef 块是创建使从 DLL 导出更简单的
// 宏的标准方法。此 DLL 中的所有文件都是用命令行上定义的 PYTHONDLL_EXPORTS
// 符号编译的。在使用此 DLL 的
// 任何其他项目上不应定义此符号。这样，源文件中包含此文件的任何其他项目都会将
// PYTHONDLL_API 函数视为是从 DLL 导入的，而此 DLL 则将用此宏定义的
// 符号视为是被导出的。
#ifdef PYTHONDLL_EXPORTS
#define PYTHONDLL_API __declspec(dllexport)
#else
#define PYTHONDLL_API __declspec(dllimport)
#endif

// 此类是从 PythonDll.dll 导出的
class PYTHONDLL_API CPythonDll {
public:
	CPythonDll(void);
	// TODO:  在此添加您的方法。
};

extern PYTHONDLL_API int nPythonDll;

PYTHONDLL_API int fnPythonDll(void);

// Caijx added.
//使用__stdcall，右键工程->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, 将其设置为__stdcall即可。
//使用__cdecl，右键工程->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, 将其设置为__cdecl即可。
extern "C"
{
	PYTHONDLL_API int add(int a, int b);
}

EXTERN_C PYTHONDLL_API int sub(int *a, int *b);

