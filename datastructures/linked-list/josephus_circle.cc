#include <iostream>

struct Node {
    int data;
    Node *next;
};

Node* generate_clist(int n) {
    Node *head = new Node;
    Node *ptr = head;
    int count = 1;
    while (--n) {
        ptr->data = count++;
        ptr->next = new Node;
        ptr = ptr->next;
    }
    ptr->data = count;
    ptr->next = head;
    return head;
}

int josephus_survivor(int n) {
    Node *head = generate_clist(n);
    Node *temp;
    
    for (int i = 1; i < n; i++) {
        temp = head->next;
        head->next = head->next->next;
        head = head->next;
        delete temp;
    }

    return head->data;
}

int main() {
    int n;

    std::cout << "Enter N: ";
    std::cin >> n;
    std::cout << "The last survivor is " << josephus_survivor(n) << std::endl;

    return 0;
}