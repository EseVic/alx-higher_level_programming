#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - it  checks if the singly- linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare= list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		turtle= turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
