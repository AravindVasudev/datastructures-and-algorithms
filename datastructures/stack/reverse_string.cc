#include <iostream>
#include <stack>

std::string reverse(const std::string& str) {
    std::stack<char> stack;
    std::string rev = "";
    for (char c : str) {
        stack.push(c);
    }
    
    while (!stack.empty()) {
        rev += stack.top();
        stack.pop();
    }

    return rev;
}

int main() {
    std::string str;

    std::cout << "Enter string: ";
    std::cin >> str;
    std::cout << reverse(str);

    return 0;
}