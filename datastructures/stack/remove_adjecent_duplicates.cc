#include <iostream>
#include <vector>

std::string remove_adjacent_duplicates(const std::string& str) {
    std::vector<char> stack;
    for (char c : str) {
        if (stack.empty() || stack.back() != c) {
            stack.push_back(c);
        } else {
            stack.pop_back();
        }
    }

    return std::string(stack.begin(), stack.end());
}

int main() {
    std::string str;

    std::cout << "Enter string: ";
    std::cin >> str;
    std::cout << "Removed Adjacent Duplicates: " << remove_adjacent_duplicates(str);

    return 0;
}