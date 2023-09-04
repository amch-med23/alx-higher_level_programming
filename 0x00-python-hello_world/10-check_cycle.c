#include "lists.h"
/**
 * check_cycle - checks it the given linked list has a cycle
 * @list: the given singely linked list
 *
 * Return: it return (0) if there is no cycle, and (1) if there is one.
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *t;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	s = list->next;
	t = s->next;
	while (s != NULL && t != NULL && t->next != NULL)
	{
		if (s == t)
		{
			return (1);
		}
		s = s->next;
		t = t->next->next;
	}
	return (0);
}
