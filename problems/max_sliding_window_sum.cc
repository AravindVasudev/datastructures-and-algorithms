#include <iostream>
#include <vector>
#include <cmath>

int max_window_sum(const std::vector<int>& arr, const int k) {
    if (arr.size() < k) return -1;

    // window sum
    int max_sum = 0;
    for (int i = 0; i < k; i++) max_sum += arr[i];

    int window_sum = max_sum;
    for (int i = k; i < arr.size(); i++) {
        window_sum += arr[i] - arr[i - k];
        max_sum = std::max(max_sum, window_sum);
    }

    return max_sum;
}

int main() {
    std::vector<int> arr;
    int window_size, input;

    std::cout << "Enter window size: ";
    std::cin >> window_size;

    std::cout << "Enter elements (-9999 to quit): \n";
    while (std::cin >> input && input != -9999) {
        arr.push_back(input);
    }

    std::cout << "The max window sum is " << max_window_sum(arr, window_size);
}
