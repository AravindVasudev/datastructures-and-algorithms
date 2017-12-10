#include <iostream>
#include <queue>
#include <stack>
#include <sstream>

void reverse(std::queue<int>& q) {
    std::stack<int> s;

    while (!q.empty()) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }
}

void reverse_recursive(std::queue<int>& q) {
    if (q.empty()) return;

    int temp = q.front();
    q.pop();
    reverse_recursive(q);
    q.push(temp);
}

std::string visualize(std::queue<int> q) {
    std::stringstream os;

    while (!q.empty()) {
        os << q.front() << " ";
        q.pop();
    }

    return os.str();
}

int main() {
    std::queue<int> q;

    for (int i = 10; i > 0; i--) q.push(i);
    std::cout << visualize(q) << std::endl;

    reverse(q);
    std::cout << visualize(q) << std::endl;


    reverse_recursive(q);
    std::cout << visualize(q) << std::endl;
}
