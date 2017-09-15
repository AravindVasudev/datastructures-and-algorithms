/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method  
  Node *temp = NULL, *next;
  while (head) {
    next = head->next;
    head->next = temp;
    temp = head;
    head = next;
  }
  
  return temp;
}
