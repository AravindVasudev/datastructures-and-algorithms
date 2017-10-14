#include <iostream>
#include <cstdlib>
#include <functional>
#include <locale>
#include <stack>
#include <map>

int evaluate_postfix(std::string expression) {
    std::stack<int> stack;
    std::map<char, std::function<int(const int&, const int&)>> operation;
    int a, b;

    operation['+'] = [](int a, int b) { return a + b; };
    operation['-'] = [](int a, int b) { return a - b; };
    operation['*'] = [](int a, int b) { return a * b; };
    operation['/'] = [](int a, int b) { return a / b; };    

    for (char c : expression) {
        if (isdigit(c)) stack.push(c - '0');
        else {
            a = stack.top(); stack.pop();
            b = stack.top(); stack.pop();
            stack.push(operation[c](b, a));
        }
    }

    return stack.top();
}

int main() {
    std::string expression;

    std::cout << "Enter expression: ";
    std::cin >> expression;
    std::cout << expression << " => " << evaluate_postfix(expression) << "\n";

    return 0;
}