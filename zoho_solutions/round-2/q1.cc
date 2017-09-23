#include <iostream>
#include <cstdlib>

int main() {
    int sides[4];
    for (int i = 0; i < 4; i++) {
        std::cin >> sides[i];

        if (sides[i] < 1) {
            std::cerr << "Invalid Input.";
            exit(0);
        }
    }

    if (sides[0] == sides[2] && sides[1] == sides[3]) {
        if (sides[0] == sides[1]) {
            std::cout << "Square";
        } else {
            std::cout << "Rectangle";
        }
    } else {
        std::cout << "Neither";
    }

    return 0;
}
