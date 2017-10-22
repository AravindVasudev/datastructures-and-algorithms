#include <iostream>
#include <vector>
#include <stack>

std::string printer(const std::vector<int>& arr) {
    std::string visualize = "[ ";
    for (int i : arr) {
        visualize += std::to_string(i) + " ";
    }

    return visualize + "]";
}

std::vector<int> calculate_span_inefficient(const std::vector<int>& arr) {
    std::vector<int> s;
    int curSpan = 1;

    s.push_back(1);
    for (int i = 1; i < arr.size(); i++) {
        curSpan = 1;
        for (int j = i - 1; (j >= 0) && (arr[i] >= arr[j]); j--) {
            curSpan++;
        }
        s.push_back(curSpan);
    }

    return s;
}

std::vector<int> calculate_span_efficient(const std::vector<int>& arr) {
    std::stack<int> stack;
    std::vector<int> s;

    stack.push(0);
    s.push_back(1);
    for (int i = 1; i < arr.size(); i++) {
        while (!stack.empty() && arr[stack.top()] <= arr[i]) {
            stack.pop();
        }
        s.push_back(stack.empty() ? i + 1 : i - stack.top());
        stack.push(i);
    }

    return s;
}

int main() {
    std::vector<int> arr;
    int input;

    std::cout << "Enter elements: (Ctrl + Z to stop)\n";
    while (std::cin >> input) {
        arr.push_back(input);
    }

    std::cout
        << "Inefficient solution: " 
        << printer(calculate_span_inefficient(arr)) 
        << std::endl
        << "  Efficient solution: " 
        << printer(calculate_span_efficient(arr)) 
        << std::endl;

    return 0;
}