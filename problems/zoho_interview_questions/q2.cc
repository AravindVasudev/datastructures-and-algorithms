#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr, peaks;
    int input;

    std::cout << "Enter elements (-9999 to break):\n";
    while (std::cin >> input && input != -9999) {
        arr.push_back(input);
    }

    std::cout << "Enter peak positions (-ve to break):\n";
    while (std::cin >> input && input >= 0 && input < arr.size()) {
        peaks.push_back(input);
    }

    std::vector<int>::iterator prev_peak = arr.begin(), cur_peak;
    for (const auto& peak : peaks) {
        cur_peak = arr.begin() + peak + 1;
        std::sort(prev_peak, cur_peak);
        prev_peak = cur_peak;
    }

    for (const auto& el : arr) {
        std::cout << el << " ";
    }
}
