#include <iostream>
#include <stack>

int main() {
    std::stack<long> stack, max;
    long n, option, data;
    
    std::cin >> n;
    while (n--) {
        std::cin >> option;
        switch(option) {
            case 1:
                std::cin >> data;
                stack.push(data);
                if (max.empty() || data >= max.top()) max.push(data);
                break;
            case 2:
                if (stack.top() == max.top()) max.pop();
                stack.pop();
                break;
            case 3:
                std::cout << max.top() << "\n";
                break;
        }
    }
    
    return 0;
}