#include <iostream>
#include <algorithm>

std::string base_7(int n) {
    std::string base7;
    char map[] = "abcdefg";

    while (n > 0) {
        base7 += map[n % 7];
        n /= 7;
    }

    std::reverse(base7.begin(), base7.end());
    return base7;
}

int main() {
    int n;

    std::cout << "Enter n: ";
    std::cin >> n;
    std::cout << base_7(n);

    return 0;
}
