#include <iostream.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

void encrypt(char text[]) {
    char odd[50], even[50];
    int i, odd_top, even_top;
    odd_top = even_top = 0;

    for (i = 0; text[i]; i++) {
	if (i & 1) odd[odd_top++] = text[i];
	else even[even_top++] = text[i];
    }

	odd[odd_top] = even[even_top] = '\0';

	cout << "\t Cipher Text: "<< even << odd;
}

void decrypt(char cipher[]) {
	char text[100];
	int length = strlen(cipher), i, text_top = 0;

	if (length & 1) length = (length / 2) + 1;
	else length /= 2;

	for (i = 0; i < length; i++) {
		text[text_top] = cipher[i];
		text_top += 2;
	}

	for (i = length, text_top = 1; text[i]; i++) {
		text[text_top] = cipher[i];
		text_top += 2;
	}

	cout << "\t Plain Text: " << text;
}

void main() {
	char text[100], choice;

	clrscr();

	cout << "\n\t\t\t|----- 2 RAIL FENCE TECHNIQUE -----|";
	cout << "\n\t Encrypt / Decrypt (E / D): ";
	cin >> choice;
	cout << "\t Enter text: ";
    cin >> text;

    tolower(choice) == 'e' ? encrypt(text) : decrypt(text);
    getch();
}