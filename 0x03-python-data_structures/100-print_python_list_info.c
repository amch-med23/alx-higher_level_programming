#include <Python.h>
/**
* print_python_list_info - prints some infos about a given pytohn list
* @p: the given python object
*
* Return: nothing (void)
**/

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int i, size, allocp;

	size = Py_SIZE(p);
	allocp = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocp);
	i = 0;
	while (i < size)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
