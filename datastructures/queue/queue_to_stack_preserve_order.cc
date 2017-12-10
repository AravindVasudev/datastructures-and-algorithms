#include <iostream>
#include <stack>
#include <queue>

void queue_to_stack(std::queue<int>& q, std::stack<int>& s) {
    while (!q.empty()) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }

    while (!q.empty()) {
        s.push(q.front());
        q.pop();
    }
}

int main() {
    std::queue<int> q;
    std::stack<int> s;

    for (int i = 1; i < 11; i++) q.push(i);

    queue_to_stack(q, s);
    while (!s.empty()) {
        std::cout << s.top() << " ";
        s.pop();
    }

    return 0;
}
