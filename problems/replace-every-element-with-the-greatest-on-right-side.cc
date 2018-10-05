#include <iostream>
#include <vector>
#include <climits>

std::string visualize(const std::vector<int>& arr) {
    std::string visualize = "[ ";
    for (int i : arr) {
        visualize += std::to_string(i) + " ";
    }

    return visualize + "]";
}

std::vector<int> replace_with_greatest_on_right_naive(std::vector<int>& arr) {
    std::vector<int> replaced;

    for (int i = 0; i < arr.size(); i++) {
        int max = INT_MIN;
        for (int j = i + 1; j < arr.size(); j++) {
           if (max < arr[j]) max = arr[j];
        }

        replaced.push_back(i == arr.size() - 1? -1 : max);
    }

    return replaced;
}


std::vector<int> replace_with_greatest_on_right_efficient(std::vector<int>& arr) {
    std::vector<int> replaced(arr.size());
    int max = arr.back();

    replaced.back() = -1;
    for (int i = arr.size() - 2; i >= 0; i--) {
        replaced[i] = max;

        if (max < arr[i]) max = arr[i];
    }

    return replaced;
}

int main() {
    std::vector<int> arr;
    int input;

    std::cout << "Enter elements (EOF to stop):\n";
    while (std::cin >> input) {
        arr.push_back(input);
    }

    std::cout << "    Naive: " << visualize(replace_with_greatest_on_right_naive(arr)) << std::endl;
    std::cout << "Efficient: " << visualize(replace_with_greatest_on_right_efficient(arr)) << std::endl;

    return 0;
}
