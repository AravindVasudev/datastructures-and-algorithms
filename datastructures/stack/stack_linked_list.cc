#include <iostream>

struct Node {
    int data;
    Node *next;
};

class Stack {
   Node *head;

public:
    Stack() {
        head = NULL;
    }

    bool is_empty() {
        return !head;
    }

    void push(int x) {
        head = new Node{x, head};
    }

    int pop() {
        if (is_empty()) return -1;
        Node *temp = head;
        head = head->next;
        int data = temp->data;
        delete temp;
        return data;
    }

    int peek() {
        if (is_empty()) return -1;
        return head->data;
    }
};

int main() {
    Stack s;

    std::cout << "is_empty(): " << s.is_empty() << "\n";
 
    for (int i = 1; i < 11; i++) s.push(i);
    std::cout << "peek(): " << s.peek() << " pop(): " << s.pop() << "\n";

    return 0;
}
