/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
  Node *slow = head, *fast = head;
  while (fast != NULL) {
    slow = slow->next;
    fast = fast->next->next;
    
    if (slow == fast) return 1;
  }
  
  return 0;
}
