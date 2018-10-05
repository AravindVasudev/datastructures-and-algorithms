#include <iostream>
#include <cstdlib>
#include <set>

int main() {
    int sides[4];
    for (int i = 0; i < 4; i++) {
        std::cin >> sides[i];

        if (sides[i] < 1) {
            std::cerr << "Invalid Input.";
            exit(0);
        }
    }

    std::set<int> sides_set{std::begin(sides), std::end(sides)};
    switch (sides_set.size()) {
        case 1:
            std::cout << "Square";
            break;
        case 2:
            std::cout << "Rectangle";
            break;
        default:
            std::cout << "Neither";
    }

    return 0;
}
