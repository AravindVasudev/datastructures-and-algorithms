#include <stdio.h>
#include <stdlib.h>

struct CLL {
    int data;
    struct CLL *next;
};

void push(struct CLL *head, int data) {
    struct CLL *current = head;
    struct CLL *new_node = (struct CLL*) malloc( sizeof(struct CLL) );

    new_node->data = data;
    while ( current->next != head) current = current->next;
    new_node->next = new_node;

    if (head == NULL) head = new_node;
    else {
        new_node->next = head;
        current->next = new_node;
    }
}

void unshift(struct CLL **head, int data) {
    struct CLL *current = *head;
    struct CLL *new_node = (struct CLL*) malloc( sizeof(struct CLL) );

    new_node->data = data;
    while (current->next != *head) current = current->next;

    if (*head == NULL) *head = new_node;
    else {
        new_node->next = *head;
        current->next = new_node;
        *head = new_node;
    }
}

int pop(struct CLL *head) {
    struct CLL *current = head;
    struct CLL *temp;
    int data;

    if (head == NULL) return -1;
    while (current->next->next != head) current = current->next;

    temp = current->next;
    current->next = head;
    data = temp->data;
    free(temp);

    return data;
}

int shift(struct CLL **head) {
    struct CLL *current = *head;
    struct CLL *temp;
    int data;

    if (*head == NULL) return -1;
    while (current->next != *head) current = current->next;
    temp = *head;
    *head = (*head)->next;
    current->next = *head;

    data = temp->data;
    free(temp);

    return data;
}

void display(struct CLL *head) {
    struct CLL *current = head;

    if (head == NULL) return;

    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != head);

    printf("\n");
}

int main() {
    struct CLL *list = (struct CLL*) malloc( sizeof(struct CLL) );
    list->data = 6;
    list->next = list;

    push(list, 1);
    push(list, 2);
    push(list, 3);
    push(list, 4);
    push(list, 5);
    display(list);

    pop(list);
    pop(list);
    shift(&list);
    unshift(&list, 7);
    display(list);

    return 0;
}
