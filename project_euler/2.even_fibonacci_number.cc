#include <iostream>
#define LIMIT 4000000

int main() {
    /* int prev1 = 0; */
    /* int prev2 = 1; */
    /* int cur = 0; */
    /* int sum = 0; */

    /* while (cur < LIMIT) { */
    /*     cur = prev1 + prev2; */
    /*     prev2 = prev1; */
    /*     prev1 = cur; */

    /*     if (!(cur % 2)) { */
    /*         sum += cur; */
    /*     } */
    /* } */

    int sum = 0, a = 1, b = 1, c = 2;
    while (c < LIMIT) {
        sum += c;
        a = b + c;
        b = c + a;
        c = a + b;
    }

    std::cout << sum;
    return 0;
}
