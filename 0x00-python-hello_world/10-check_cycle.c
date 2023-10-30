#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next; // Move one step
        fast = fast->next->next; // Move two steps

        // If there is a cycle, the fast pointer will eventually catch up to the slow pointer
        if (slow == fast)
            return 1;
    }

    // If we reach here, there is no cycle
    return 0;
}
