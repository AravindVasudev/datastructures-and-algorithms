#include <stdio.h>
#include <string.h>

void x_printer(char *str) {
    int len = strlen(str);

    for (int i = 0, j = len - 1; i <= len, j >= 0; i++, j--) {
        if (i < j) {
            for (int x = 0; x < i; x++) printf(" ");
            printf("%c", str[i]);
            for (int x = 0; x < j - i - 1; x++) printf(" ");
            printf("%c\n", str[j]);
        }

        if (i == j) {
            for (int x = 0; x < i; x++) printf(" ");
            printf("%c\n", str[i]);
        }

        if (i > j) {
            for (int x = j - 1; x >= 0; x--) printf(" ");
            printf("%c", str[j]);
            for (int x = 0; x < i - j - 1; x++) printf(" ");
            printf("%c\n", str[i]);
        }
    }
}

int main() {
    char str[100];
    scanf("%s", str);
    x_printer(str);

    return 0;
}
