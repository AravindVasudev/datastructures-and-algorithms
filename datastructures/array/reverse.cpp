#include <iostream>

int main() {
	int n;
	std::cout << "Enter N: ";
	std::cin >> n;

	int arr[n];
	for (int i = 0; i < n; i++) std::cin >> arr[i];

	int i = 0, j = n - 1, temp;
	while (i < j) {
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
		i++; j--;
	}

	for (i = 0; i < n; i++) std::cout << arr[i] << " ";

	return 0;
}