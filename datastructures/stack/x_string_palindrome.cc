#include <iostream>
#include <stack>

bool is_palindrome(std::string str) {
    std::stack<char> stack;
    int i = -1;

    while (str[++i] != 'X') {
        stack.push(str[i]);
    }

    while (str[++i]) {
        if (stack.empty() || stack.top() != str[i]) {
            return false;
        }

        stack.pop();
    }

    return stack.empty();
}

int main() {
    std::string str;

    std::cout << "Enter X format string (zXz): ";
    std::cin >> str;

    std::cout << str << " => " << is_palindrome(str) << std::endl;

    return 0;
}