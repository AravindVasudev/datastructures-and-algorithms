#include <iostream>
#include <vector>

void read_into_vec(std::vector<int>& vec, const int& n) {
    for (int i = 0; i < n; i++) {
        std::cin >> vec[n];
    }
}

int main() {
    int n1, n2, n3;

    std::cin >> n1 >> n2 >> n3;
    std::vector<int> v1(n1), v2(n2), v3(n3);

    read_into_vec(v1, n1);
    read_into_vec(v2, n2);
    read_into_vec(v3, n3);

    for (auto i : v1) std::cout << i;
    std::cout << "\n";
    for (auto i : v2) std::cout << i;

    std::cout << "\n";
    for (auto i : v3) std::cout << i;
}
