#include <stdio.h>

/**
 * 1. Move `N - 1` disks to aux tower using to tower as aux ( smaller problem )
 * 2. Move base disk to to tower ( base problem )
 * 3. Move `N - 1` disks back to to tower using from tower as aux ( smaller problem )
 **/
void towers_of_hanoi(int n, char from, char to, char aux) {
    if (n == 1)
        printf("\n %c -> %c", from, to);
    else {
        towers_of_hanoi(n - 1, from, aux, to);
        towers_of_hanoi(1, from, to, aux);
        towers_of_hanoi(n - 1, aux, to, from);
    }
}

int main() {
    int n;

    printf("Enter N: ");
    scanf("%d", &n);
    towers_of_hanoi(n, 'A', 'C', 'B');

    return 0;
}
