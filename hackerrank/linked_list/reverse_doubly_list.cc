/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // Complete this function
    // Do not write the main method.
  Node *cur, *next, *prev;
  if (head == NULL) return NULL;
  cur = head;
  prev = NULL;
  while (cur != NULL) {
    next = cur->next;
    cur->next = prev;
    cur->prev = next;
    prev = cur;
    cur = next;
  }
  
  return prev;
}
