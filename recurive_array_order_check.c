#include <stdio.h>

int is_sorted(int a[], int n) {
    if (n == 1) return 1; // base case
    return (a[n - 1] <= a[n - 2]) ? 0 : is_sorted(a, n - 1); // recursive case
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int b[5] = {1, 2, 3, 5, 4};

    printf("%d\t%d", is_sorted(a, 5), is_sorted(b, 5));
}
