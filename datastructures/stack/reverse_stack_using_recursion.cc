#include <iostream>
#include <stack>

void insert_at_bottom(std::stack<int>& s, int temp) {
    if (s.empty()) {
        s.push(temp);
        return;
    }

    int data = s.top(); s.pop();
    insert_at_bottom(s, temp);
    s.push(data);
}

void reverse(std::stack<int>& s) {
    if (s.empty()) return;
    int temp = s.top(); s.pop();
    reverse(s);
    insert_at_bottom(s, temp);
}

int main() {
    std::stack<int> s;

    for (int i = 10; i > 0; i--) s.push(i);

    reverse(s);
    while(!s.empty()) {
        std::cout << s.top() << " ";
        s.pop();
    }

    return 0;
}