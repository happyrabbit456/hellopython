// ���� ifdef ���Ǵ���ʹ�� DLL �������򵥵�
// ��ı�׼�������� DLL �е������ļ��������������϶���� PYTHONDLL_EXPORTS
// ���ű���ġ���ʹ�ô� DLL ��
// �κ�������Ŀ�ϲ�Ӧ����˷��š�������Դ�ļ��а������ļ����κ�������Ŀ���Ὣ
// PYTHONDLL_API ������Ϊ�Ǵ� DLL ����ģ����� DLL ���ô˺궨���
// ������Ϊ�Ǳ������ġ�
#ifdef PYTHONDLL_EXPORTS
#define PYTHONDLL_API __declspec(dllexport)
#else
#define PYTHONDLL_API __declspec(dllimport)
#endif

// �����Ǵ� PythonDll.dll ������
class PYTHONDLL_API CPythonDll {
public:
	CPythonDll(void);
	// TODO:  �ڴ�������ķ�����
};

extern PYTHONDLL_API int nPythonDll;

PYTHONDLL_API int fnPythonDll(void);

// Caijx added.
//ʹ��__stdcall���Ҽ�����->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, ��������Ϊ__stdcall���ɡ�
//ʹ��__cdecl���Ҽ�����->Properties->Configuration Properties->C / C++->Advanced->Calling Convention, ��������Ϊ__cdecl���ɡ�
extern "C"
{
	PYTHONDLL_API int add(int a, int b);
}

EXTERN_C PYTHONDLL_API int sub(int *a, int *b);

