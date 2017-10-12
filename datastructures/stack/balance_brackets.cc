#include <iostream>
#include <stack>
#include <map>

int main() {
    std::stack<char> s;
    std::string expression;
    std::map<char, char> get_pair;
    bool flag = true;

    get_pair[')'] = '(';
    get_pair['}'] = '{';
    get_pair[']'] = '[';

    std::cout << "Input Expression: ";
    std::cin >> expression;

    for (char c : expression) {
        if (c == '(' || c == '{' || c == '[') s.push(c);
        if (c == ')' || c == '}' || c == ']') {
            if (!s.empty() && get_pair[c] == s.top()) s.pop();
            else {
                flag = false;
                break;
            }
        }
    }

    if (!s.empty()) flag = false;
    std::cout << expression << " => " << flag;

    return 0;
}