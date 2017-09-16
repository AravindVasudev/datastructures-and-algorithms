/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function 
    // Do not write the main method
  Node *curA = headA, *curB = headB;
  int lenA = 0, lenB = 0;  
  while (curA != NULL) {
    curA = curA->next;
    lenA++;
  }
  
    while (curB != NULL) {
    curB = curB->next;
    lenB++;
  }
  
  if (lenA < lenB ) {
    Node *temp = headA;
    headA = headB;
    headB = temp;
  }
  
  int diff = abs(lenA - lenB);
  for (int i = 0; i < diff; i++) headA = headA->next;
  
  while (headA != NULL && headB != NULL) {
    if (headA == headB) return headA->data;
    headA = headA->next;
    headB = headB->next;
  }
  
  return -1;
  
}
