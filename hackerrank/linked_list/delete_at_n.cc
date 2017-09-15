/*
  Delete Node at a given position in a linked list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
  // Complete this method
  if (position == 0) {
    auto next = head->next;
    delete head;
    return next;
  }

  head->next = Delete(head->next, position - 1);
  return head;
}
