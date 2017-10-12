#include <iostream>

class Stack {
    int top;
    int size;
    int *arr;

public:
    Stack() {
        top = -1;
        size = 10;
        arr = new int[size];
    }

    Stack(int n) {
        top = -1;
        size = n;
        arr = new int[size];
    }

    bool is_empty() {
        return top == -1;
    }

    bool is_full() {
        return top == size - 1;
    }

    int get_size() {
        return size;
    }

    int peek() {
        return arr[top];
    }

    void push(int x) {
        if (is_full()) return;
        arr[++top] = x;
    }

    int pop() {
        if (is_empty()) return -1;
        return arr[top--];
    }
};

int main() {
    Stack s;

    std::cout << "is_empty(): " << s.is_empty() << " is_full(): " << s.is_full() << "\n";
    
    for (int i = 1; i < 11; i++) s.push(i);
    s.push(11);
    std::cout << "peek(): " << s.peek() << " pop(): " << s.pop() << "\n";
    std::cout << "get_size(): " << s.get_size() << " peek(): " << s.peek() << "\n";

    Stack fs(3);
    fs.push(1);
    fs.push(2);
    fs.push(3);
    fs.push(4);
    std::cout << "peek(): " << fs.peek() << " pop(): " << fs.pop() << "\n";
    fs.pop(); fs.pop();
    std::cout << "is_empty(): " << fs.is_empty() << " pop(): " << fs.pop() << "\n";

    return 0;
}