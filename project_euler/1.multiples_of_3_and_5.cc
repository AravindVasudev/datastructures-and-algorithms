#include <iostream>
#define LIMIT 1000

int sumDivisibleBy(const int& n) {
    const int p = LIMIT / n;
    return (n * p * (p + 1)) / 2;
}

int main() {
    /* int count = 0; */
    /* for (int i = 1; i < LIMIT; i++) { */
    /*     if (!(i % 3) || !(i % 5)) { */
    /*         count += i; */
    /*     } */
    /* } */

    std::cout << sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15);
    return 0;
}
