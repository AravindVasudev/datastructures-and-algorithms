#include <iostream>

struct Node {
    int data;
    Node *next;
};

class Queue {
    Node *front, *rear;

public:
    Queue() {
        front = rear = NULL;
    }

    bool is_empty() {
        return front == NULL;
    }

    int get_front() {
        return front->data;
    }

    void enqueue(int data) {
        Node *newNode = new Node{data, NULL};
        if (rear == NULL) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = rear->next;
        }
    }

    int dequeue() {
        if (is_empty()) return -1;

        int data = front->data;
        Node *temp = front;
        front = front->next;
        delete temp;

        return data;
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
