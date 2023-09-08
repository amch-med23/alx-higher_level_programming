#include "lists.h"
/**
 * rev_listint - reverses a linked list
 * @head: a pointer to the first node of the list
 *
 * Return: it returns a pointer to the fisrt node in the new list
 */
void rev_listint(listint_t **head)
{
	listint_t *p = NULL;
	listint_t *c = *head;
	listint_t *n = NULL;

	while (c)
	{
		n = c->next;
		c->next = p;
		p = c;
		c = n;
	}
	*head = p;
}
/**
 * is_palindrome - determines if a list is palindrome or not
 * @head: the pointer to the linked list
 *
 * Return: 1 if it is, 0 else
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl = *head, *fa = *head, *dup = NULL, *tmp = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fa = fa->next->next;
		if (!fa)
		{
			dup = sl->next;
			break;
		}
		if (!fa->next)
		{
			dup = sl->next->next;
			break;
		}
		sl = sl->next;
	}
	rev_listint(&dup);
	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
		{
			return (0);
		}
	}
	if (!dup)
	{
		return (1);
	}
	return (0);
}
