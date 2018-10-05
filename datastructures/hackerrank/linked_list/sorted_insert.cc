/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head,int data)
{
    // Complete this function
   // Do not write the main method. 
  Node *new_node = new Node{data, NULL, NULL};
  
  if (head == NULL) return new_node;
  if (head->data > data) {
    new_node->next = head;
    head->prev = new_node;
    return new_node;
  }
  
  Node *n1 = NULL, *n2 = head;
  while (n2 != NULL && n2->data < data) {
    n1 = n2;
    n2 = n2->next;
  }
  
  if (n2 == NULL) {
    n1->next = new_node;
    new_node->prev = n1;
  } else {
    n1->next = new_node;
    n2->prev = new_node;
    new_node->prev = n1;
    new_node->next = n2;
  }
  
  return head;
  
}
