#include<iostream>
using namespace std;

int main() {
	// get n
	int n;
	cin >> n;

	// init and read array in reverse
	int arr[n];
	for(int i = n - 1; i >= 0; i--) {
		cin >> arr[i];
	}

	// print array
	for(int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
}
