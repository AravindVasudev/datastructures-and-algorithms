#include <iostream>
#include <sstream>
#include <cmath>

std::string bottom_left_diamond(const int& nstars) {
    std::stringstream output;
    const int n = ceil(sqrt(nstars));
    const int length = 2 * n - 1;
    int print_start_indicator = n * n;

    for (int i = 1; i <= length / 2 + 1; i++) {
        output << std::string(n - i, ' ');
        for (int j = 0; j < i; j++) {
            output << (print_start_indicator-- > nstars ? "  " : "* ");
        }
        output << "\n";
    }

    for (int i = length / 2; i > 0; i--) {
        output << std::string(n - i, ' ');
        for (int j = 0; j < i; j++) {
            output << (print_start_indicator-- > nstars ? "  " : "* ");
        }
        output << "\n";
    }

    return output.str();
}

int main() {
    int n;

    std::cout << "Enter N: ";
    std::cin >> n;
    std::cout << bottom_left_diamond(n);

    return 0;
}
