#include <iostream>
#include <vector>
#include <sstream>

std::string n_inner_square(const int& n) {
    int length = 2 * n - 1;
    std::vector<int> line(length);
    std::stringstream output;

    auto line_to_output = [&output, &line]() {
        for (const auto& el : line) {
            output << el << " ";
        }
        output << "\n";
    };

    for (int i = 0; i < length; i++) {
        line[i] = n;
    }

    line_to_output();
    for (int i = 1; i < length / 2 + 1; i++) {
        for (int j = i; j < length - i; j++) {
            line[j]--;
        }

        line_to_output();
    }

    for (int i = length / 2; i > 0; i--) {
        for (int j = i; j < length - i; j++) {
            line[j]++;
        }

        line_to_output();
    }

    return output.str();
}

int main() {
	int n;

	std::cout << "Enter n: ";
	std::cin >> n;
	std::cout << n_inner_square(n);

	return 0;
}
