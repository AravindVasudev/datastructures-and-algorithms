#include <stdio.h>

char A[100];

void binary(int n) {
    if (n < 1) printf("%s\n", A);
    else {
        A[n - 1] = '0';
        binary(n - 1);
        A[n - 1] = '1';
        binary(n - 1);
    }
}

int main() {
    int n;

    printf("Enter N: ");
    scanf("%d", &n);
    binary(n);

    return 0;
}
