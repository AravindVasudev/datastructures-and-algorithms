#include <iostream>
#include <stack>

std::stack<int> reverse(std::stack<int> s) {
    std::stack<int> rev;
    while (!s.empty()) {
        rev.push(s.top()); s.pop();
    }

    return rev;
}

int main() {
    std::stack<int> s;

    for (int i = 10; i > 0; i--) s.push(i);

    s = reverse(s);
    while (!s.empty()) {
        std::cout << s.top() << " ";
        s.pop();
    }
}