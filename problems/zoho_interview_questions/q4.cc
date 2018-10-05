#include <iostream>
#include <vector>
#include <map>

int main() {
    std::vector<int> arr;
    std::map<int, int> count;
    int input;

    while (std::cin >> input && input != -9999) {
        arr.push_back(input);
        count[input]++;
    }

    std::cin >> input;
    std::cout << "Count of " << input << " is " << count[input];

    return 0;
}
