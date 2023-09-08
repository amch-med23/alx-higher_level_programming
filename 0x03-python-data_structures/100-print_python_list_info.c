#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some infos about a python linked list
 * @p: the given python object
 *
 * Return: nothing (void)
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	int x;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	x = 0;
	while (x < size)
	{
		printf("Element: %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
		x++;
	}
}
