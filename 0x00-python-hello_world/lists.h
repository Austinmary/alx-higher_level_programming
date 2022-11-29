#ifndef LIST_H
#define LIST_H
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

/**
 * struct listint_s - singlylinked list
 * @n: int value stored
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif

#include "lists.h"

/**
 * check_cycle - finds the index at which a loop starts
 * @head: list head
 *
 * Return: 0 if no cycle 1 if there is cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *fast = head, *slow = head;

	if (!head || !(head->next))
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
