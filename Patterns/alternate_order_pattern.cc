/**
 * I/P: 4
 * O/P:
 * 01 02 03 04
 * 09 10 11 12
 * 13 14 15 16
 * 05 06 07 08
 *
 * I/P: 5
 * O/P:
 * 01 02 03 04 05
 * 11 12 13 14 15
 * 21 22 23 24 25
 * 16 17 18 19 20
 * 06 07 08 09 10
 **/

#include <iostream>
#include <vector>
#include <cmath>
#include <sstream>

std::string alternate_order_pattern(const int& n) {
    std::stringstream output;

    for (int i = 0; i < n; i += 2) {
        int k = i * n + 1;
        for (int j = k; j < k + n; j++) {
            if (j < 10) {
                output << "0";
            }
            output << j << " ";
        }
        output << "\n";
    }

    int m = n & 1 ? n - 2 : n - 1;
    for (int i = m; i > 0; i -= 2) {
        int k = i * n + 1;
        for (int j = k; j < k + n; j++) {
            if (j < 10) {
                output << "0";
            }
            output << j << " ";
        }
        output << "\n";
    }

    return output.str();
}

int main() {
    int n;

    std::cout << "Enter N: ";
    std::cin >> n;
    std::cout << alternate_order_pattern(n);

    return 0;
}
