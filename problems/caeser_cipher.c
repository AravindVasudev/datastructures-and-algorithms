#include <stdio.h>
#include <conio.h>
#include <ctype.h>

void caesar_cipher(char *text, int shift, int to_encrypt) {
	int i, ascii_shift;

	if (!to_encrypt) {
		shift *= -1;
	}
	for (i = 0; text[i]; i++) {
		ascii_shift = isupper(text[i]) ? 65 : 97;
		text[i] = ((text[i] + shift - ascii_shift) % 26) + ascii_shift;
	}
}

void main() {
	char text[100], choice;
	int shift;

	clrscr();

	printf("Encrypt / Decrypt (E / D): ");
	scanf("%c", &choice);

	printf("Enter text: ");
	scanf("%s", text);

	printf("Enter shift key: ");
	scanf("%d", &shift);

	caesar_cipher(text, shift, tolower(choice) == 'e');
	printf("Encrypted Text: %s", text);

	getch();
}