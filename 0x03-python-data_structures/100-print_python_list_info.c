#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints size, alloc, and elements of list
 * @p: pointer to list
 */
void print_python_list_info(PyObject *p)
{
	int size, i;
	Py_ssize_t alloc;
	PyObject *item;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", alloc);
	if (PyList_Check(p))
	{
		for (i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
