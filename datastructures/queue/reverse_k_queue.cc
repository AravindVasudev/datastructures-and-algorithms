#include <iostream>
#include <queue>
#include <stack>
#include <sstream>

std::string visualize(std::queue<int> q) {
    std::stringstream os;

    while (!q.empty()) {
        os << q.front() << " ";
        q.pop();
    }

    return os.str();
}

void reverse_k(std::queue<int>& q, int n) {
    if (q.empty() || n < 0 || n > q.size()) return;
    int diff = q.size() - n;

    std::stack<int> s;

    while (n--) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }

    while (diff--) {
        q.push(q.front());
        q.pop();
    }
}

int main() {
    std::queue<int> q;

    for (int i = 1; i <= 10; i++) q.push(i);
    std::cout << visualize(q) << std::endl;

    reverse_k(q, 5);
    std::cout << visualize(q) << std::endl;

    return 0;
}
