/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
  // Complete this method only
  // Do not write main function. 
  if (head == NULL || position == 0) {
    return new Node{data, head};
  }
  
  Node *new_node = new Node;
  new_node->data = data;
  Node *cur = head;
  for (int i = 0; i < position - 1; i++) cur = cur->next;
  new_node->next = cur->next;
  cur->next = new_node;
  
  return head;
}
