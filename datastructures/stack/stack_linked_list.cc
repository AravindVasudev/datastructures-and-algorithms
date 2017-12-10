#include <iostream>

struct Node {
    int data;
    Node *next;
};

class Queue {
   Node *head;

public:
    Queue() {
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
    Queue q;

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);

    std::cout << " is_empty(): " << q.is_empty() << std::endl;
    std::cout << "front(): " << q.get_front() << " dequeue(): " << q.dequeue() << " dequeue(): " << q.dequeue();

    return 0;
}