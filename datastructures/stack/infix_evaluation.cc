#include <iostream>
#include <locale>
#include <cstdlib>
#include <functional>
#include <stack>
#include <map>

int evaluate_infix(std::string expression) {
    std::stack<char> operators;
    std::stack<int> operands;
    std::map<char, std::function<int(const int&, const int&)>> operation;
    std::map<char, int> precedence;

    operation['+'] = [](int a, int b) { return a + b; };
    operation['-'] = [](int a, int b) { return a - b; };
    operation['*'] = [](int a, int b) { return a * b; };
    operation['/'] = [](int a, int b) { return a / b; };    

    precedence['+'] = precedence['-'] = 1;
    precedence['*'] = precedence['/'] = 2;
    precedence['^'] = 3;

    auto perform_operation = [&]() {
        char op = operators.top(); operators.pop();
        int b = operands.top(); operands.pop();
        int a = operands.top(); operands.pop();

        operands.push(operation[op](a, b));
    };

    for (char c : expression) {
        if (c == ' ') {
             continue;
        } else if (isdigit(c)) {
            operands.push(c - '0');
        } else if (c == '(') {
            operators.push('(');
        } else if (c == ')') {
            while (operators.top() != '(') {
                perform_operation();
            }
            operators.pop();
        } else {
            while (!operators.empty() && precedence[c] <= precedence[operators.top()]) {
                perform_operation();
            }
            operators.push(c);
        }
    }

    while (!operators.empty()) {
        perform_operation();
    }

    return operands.top();
}

int main() {
    std::string expression;

    std::cout << "Enter expression: ";
    std::cin >> expression;

    std::cout << expression << " => " << evaluate_infix(expression);

    return 0;
}