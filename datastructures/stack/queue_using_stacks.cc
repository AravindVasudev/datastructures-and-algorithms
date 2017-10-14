#include <iostream>
#include <stack>

class queue {
    std::stack<int> stack1, stack2;

public:
    void enque(int x) {
        stack1.push(x);
    }

    int deque() {
        if (stack1.empty() && stack2.empty()) return -1;

        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }

        int data = stack2.top(); stack2.pop();
        return data;
    }
};

int main() {
    queue q;

    for (int i = 1; i <= 10; i++) q.enque(i);
    for (int i = 0; i < 10; i++) std::cout << q.deque() << " ";

    return 0;
}