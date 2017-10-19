#include <iostream>
#include <vector>
#include <stack>

int largest_rectangle_histogram_inefficient(const std::vector<int>& arr) {

}

int largest_rectangle_histogram_efficient(const std::vector<int>& arr) {
    
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