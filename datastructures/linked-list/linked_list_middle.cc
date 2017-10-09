#include <iostream>
#include <forward_list>

std::forward_list<int>::iterator middle(std::forward_list<int> list) {
    auto slow = list.begin();
    auto fast = list.begin();
    auto end = list.end();

    while (fast != end && std::next(fast, 1) != end) {
        std::advance(fast, 2);
        std::advance(slow, 1);
    }

    return slow;
}

int main() {
    std::forward_list<int> list;

    for (int i = 1; i <= 10; i++) {
        list.push_front(i);
    }

    std::cout << *middle(list) << std::endl;

    return 0;
}