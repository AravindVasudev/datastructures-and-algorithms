#include <iostream>
#include <queue>
#include <stack>
#include <vector>

bool stack_consecutive_pair(std::stack<int> s) {
    if (s.empty()) return false;

    if (s.size() & 1) s.pop();

    int t1, t2;
    while (!s.empty()) {
        t1 = s.top();
        s.pop();
        t2 = s.top();
        s.pop();

        if (abs(t1 - t2) != 1) return false;
    }

    return true;
}

int main() {
    std::stack<int> s;
    int input;

    std::cout << "Enter elements (-9999 to quit): \n";
    while (std::cin >> input && input != -9999) {
        s.push(input);
    }

    std::cout << stack_consecutive_pair(s);
}
