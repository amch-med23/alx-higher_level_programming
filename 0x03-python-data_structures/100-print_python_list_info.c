#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some infos about a given pytohn list
* @p: the given python object
*
* Return: nothing (void)
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	i = 0;
	whil (i < size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
