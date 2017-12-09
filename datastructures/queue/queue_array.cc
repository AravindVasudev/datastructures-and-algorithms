#include <iostream>
#include <cmath>

class Queue {
    int front, rear;
    int size;
    int *arr;

public:
    Queue() {
        front = rear = -1;
        size = 10;
        arr = new int[size];
    }

    Queue(int n) {
        front = rear = -1;
        size = n;
        arr = new int[size];
    }

    bool is_empty() {
        return front == -1;
    }

    bool is_full() {
        return ((rear + 1) % size == front);
    }

    int get_size() {
        return (size - front + rear + 1) % size;
    }

    int get_front() {
        if (is_empty()) return -1;
        return arr[front];
    }

    void enqueue(int val) {
        if (is_full()) return;

        rear = (rear + 1) % size;
        arr[rear] = val;
        if (front == -1) front = rear;
    }

    int dequeue() {
        if (is_empty()) return -1;

        int data = arr[front];
        if (front == rear) front = rear = -1;
        else front = (front + 1) % size;

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

    std::cout << "is_full(): " << q.is_full() << " is_empty(): " << q.is_empty() << std::endl;
    std::cout << "front(): " << q.get_front() << " dequeue(): " << q.dequeue() << " dequeue(): " << q.dequeue();

    return 0;
}
