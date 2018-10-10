//https://blog.csdn.net/linuxheik/article/details/51879011
//https://blog.csdn.net/sinat_27717169/article/details/80803716

#include <Python.h>

static PyObject* test_function(PyObject *self)
{
	printf("lc_hello_world test\n");
	Py_INCREF(Py_None);
	return Py_None;
}

int Add(int x, int y)
{
	return x + y;
}

static PyObject* add_function(PyObject *self, PyObject *args)
{
	int num1, num2;
	PyObject *result = NULL;
	if (!PyArg_ParseTuple(args, "ii", &num1, &num2)) {
		printf("传入参数错误！\n");
		return NULL;
	}
	result = PyLong_FromLong(num1 + num2);
	//result = Py_BuildValue("i", Add(num1, num2));
	return result;
}

static PyMethodDef lc_hello_world_methods[] = {
	{ "test", (PyCFunction)test_function, METH_NOARGS, "lc_hello_world extending test" },
	{ "add", (PyCFunction)add_function, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef lc_hello_world_module = {
	PyModuleDef_HEAD_INIT,
	"lc_hello_world",		/* name of module */
	NULL,					/* module documentation, may be NULL */
	-1,					  /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
	lc_hello_world_methods   /* A pointer to a table of module-level functions, described by PyMethodDef values. Can be NULL if no functions are present. */
};

PyMODINIT_FUNC PyInit_lc_hello_world(void)
{
	PyObject *m;
	m = PyModule_Create(&lc_hello_world_module);
	if (m == NULL)
		return NULL;
	printf("init lc_hello_world module\n");

	return m;
}




