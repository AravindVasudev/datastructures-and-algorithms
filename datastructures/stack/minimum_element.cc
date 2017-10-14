#include <iostream>
#include <stack>

class min_stack {
    std::stack<int> stack, min;
public:
    void push(int x) {
        stack.push(x);
        if (min.empty() || x < min.top()) min.push(x);
    }

    int pop() {
        if (stack.empty()) return -1;

        if (!min.empty() && stack.top() == min.top()) min.pop();
        int top = stack.top(); stack.pop();

        return top;
    }

    int minimum() {
        return min.top();
    }

    int peek() {
        return stack.top();
    }
};

int main() {
    min_stack mstack;
    
    for (int i = 10; i > 0; i--) mstack.push(i);
    
    std::cout << "min(): " << mstack.minimum() << "\n";
    mstack.pop();
    mstack.pop();
    mstack.pop();
    std::cout << "min(): " << mstack.minimum() << "\n";

    return 0;
}