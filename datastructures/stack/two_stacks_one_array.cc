#include <iostream>

class two_stack {
    int size;
    int *arr;
    int top1, top2;

public:
    two_stack() {
        size = 10;
        arr = new int[size];
        top1 = -1;
        top2 = size;
    }

    two_stack(int capacity) {
        size = capacity;
        arr = new int[size];
        top1 = 0;
        top2 = size - 1;
    }

    bool is_full() {
        return top1 == top2 - 1;
    }

    bool is_empty_1() {
        return top1 == -1;
    }

    bool is_empty_2() {
        return top2 == size;
    }

    void push1(int x) {
        if (is_full()) return;
        arr[++top1] = x;
    }

    void push2(int x) {
        if (is_full()) return;
        arr[--top2] = x;
    }

    int pop1() {
        if (is_empty_1()) return -1;
        return arr[top1--];
    }

    int pop2() {
        if (is_empty_2()) return -1;
        return arr[top2++];
    }

    int peek1() {
        if (is_empty_1()) return -1;
        return arr[top1];
    }

    int peek2() {
        if (is_empty_2()) return -1;
        return arr[top2];
    }
};

int main() {
    two_stack s;

    std::cout << "pop1(): " << s.pop1() << " pop2(): " << s.pop2() << "\n";
    
    s.push1(1); s.push1(2); s.push1(3);
    s.push2(4); s.push2(5); s.push2(6);

    std::cout << "peek1(): " << s.peek1() << " peek2(): " << s.peek2() << "\n";
    s.pop1(); s.pop1(); s.pop2();
    std::cout << "pop1(): " << s.pop1() << " pop2(): " << s.pop2() << "\n";

    return 0;
}