/*
  Merge two sorted lists A and B as one linked list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission.
  // You only need to complete this method
  if (headA == NULL) return headB;
  if (headB == NULL) return headA;

  Node *new_list, *cur;
  new_list = cur = new Node;
  while (headA != NULL && headB !=  NULL) {
    if (headA->data < headB->data) {
      cur->next = headA;
      headA = headA->next;
    } else {
      cur->next = headB;
      headB = headB->next;
    }
    cur = cur->next;
  }

  if (headA != NULL) cur->next = headA;
  if (headB != NULL) cur->next = headB;

  return new_list->next;
}
