#include <iostream>
#include <queue>

class stack {
    std::queue<int> q1, q2;

public:
    void push(int data) {
        q2.push(data);

        while(!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }

        std::queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    int pop() {
        int data = q1.front();
        q1.pop();

        return data;
    }
};


int main() {
    stack s;

    for (int i = 1; i < 11; i++) s.push(i);
    for (int i = 1; i < 5; i++) std::cout << s.pop();

    return 0;
}
