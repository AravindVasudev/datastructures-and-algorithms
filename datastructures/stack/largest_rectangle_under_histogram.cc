#include <iostream>
#include <vector>
#include <stack>
#include <climits>
#include <algorithm>

int largest_rectangle_histogram_inefficient(const std::vector<int>& arr) {
    int max = INT_MIN, left, right;

    for (int i = 0; i < arr.size(); i++) {
        left = i - 1;
        right = i + 1;

        while (left >= 0 && arr[left--] >= arr[i]);
        while (right < arr.size() && arr[right++] >= arr[i]);

        const int width = right - left - 3;
        max = std::max(width * arr[i], max);
    }

    return max;
}

int largest_rectangle_histogram_efficient(const std::vector<int>& hist) {
    std::stack<int> stack;
    int max = INT_MIN, i = 0;

    auto pop_and_update_max = [&stack, &hist, &i, &max]() {
        const int pos = stack.top();
        stack.pop();

        const int h = hist[pos];
        const int w = stack.empty() ? i : i - stack.top() - 1;
        max = std::max(h * w, max);
    };

    while (i < hist.size()) {
        if (stack.empty() || hist[i] >= hist[stack.top()]) {
            stack.push(i++);
        } else {
            pop_and_update_max();
        }
    }

    while (!stack.empty()) {
        pop_and_update_max();
    }

    return max;
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
        << largest_rectangle_histogram_inefficient(arr)
        << std::endl
        << "  Efficient solution: "
        << largest_rectangle_histogram_efficient(arr)
        << std::endl;

    return 0;
}
