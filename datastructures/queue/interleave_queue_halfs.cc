#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <sstream>

std::string visualize(std::queue<int> q) {
    std::stringstream os;

    while (!q.empty()) {
        os << q.front() << " ";
        q.pop();
    }

    return os.str();
}

void interleave_queue(std::queue<int>& q) {
    if (q.size() & 1) return;

    std::stack<int> s;
    int halfSize = q.size() / 2;

    for (int i = 0; i < halfSize; i++) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }

    for (int i = 0; i < halfSize; i++) {
        q.push(q.front());
        q.pop();
    }

    for (int i = 0; i < halfSize; i++) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();

        q.push(q.front());
        q.pop();
    }
}

void interleave_queue_2(std::queue<int>& q) {
    if (q.size() & 1) return;

    std::vector<int> s;
    int halfSize = q.size() / 2;

    for (int i = 0; i < halfSize; i++) {
        s.push_back(q.front());
        q.pop();
    }

    std::reverse(s.begin(), s.end());

    while (!s.empty()) {
        q.push(s.back());
        s.pop_back();

        q.push(q.front());
        q.pop();
    }
}

int main() {
    std::queue<int> q;
    int input;

    std::cout << "Enter the elements (-9999 to stop):\n";
    while (std::cin >> input && input != -9999) {
        q.push(input);
    }

    interleave_queue(q);
    std::cout << visualize(q) << std::endl;

    interleave_queue(q);
    std::cout << visualize(q) << std::endl;
}
