#include <iostream>
#include <locale>
#include <stack>
#include <map>

std::string infix_to_postfix(std::string expression) {
    std::stack<char> op;
    std::map<char, int> precedence;
    std::string postfix = "";

    precedence['+'] = precedence['-'] = 1;
    precedence['*'] = precedence['/'] = 2;
    precedence['^'] = 3;

    for (char c : expression) {
        if (isalnum(c)) postfix += c;
        else if (c == '(') op.push(c);
        else if (c == ')') {
            while (!op.empty() && op.top() != '(') {
                postfix += op.top();
                op.pop();
            }
            if (op.top() == '(') op.pop();
        } else {
            while (!op.empty() && precedence[c] <= precedence[op.top()]) {
                postfix += op.top();
                op.pop();
            }
            op.push(c);
        }
    }

    while (!op.empty()) {
        postfix += op.top();
        op.pop();
    }

    return postfix;
}

int main() {
    std::string expression;

    std::cout << "Enter infix expression: ";
    std::cin >> expression;

    std::cout << expression << " => " << infix_to_postfix(expression);

    return 0;
}