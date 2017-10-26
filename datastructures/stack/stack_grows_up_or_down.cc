#include <iostream>

void growth_check(int *from_main) {
    int local;
    std::cout << "from_main: " << from_main << " local: " << &local << std::endl;

 << std::endl    std::cout << "growing " << (from_main < &local ? "up" : "down") << "wards";
}

int main() {
    int local;
    growth_check(&local);
}
