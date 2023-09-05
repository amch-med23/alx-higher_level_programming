#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert's a node in the linked list
 * @head: the head of the list
 * @n: the number to insert
 *
 * Return: a modified linked list of type listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *h;

	h = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (h)
	{
		if (h->n > number)
		{
			break;
		}
		prev = h;
		h = h->next;
	}
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	} else
	{
		new->next = h;
		if (h == *head)
		{
			*head = new;
		}
		else
			prev->next = new;
	}
	return (new);
}
