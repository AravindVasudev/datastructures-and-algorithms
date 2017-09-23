#include <iostream>

void merge(int arr[], int l, int m, int u) {
    int n1 = m - l + 1;
    int n2 = u - m;
    int i, j, k;

    int left[n1], right[n2];
    for (i = 0; i < n1; i++) {
        left[i] = arr[l + i];
    }

    for (j = 0; j < n2; j++) {
        right[j] = arr[m + 1 + j];
    }

    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }

    while (i < n1) {
        arr[k++] = left[i++];
    }

    while(j < n2) {
        arr[k++] = right[j++];
    }
}

void mergesort(int arr[], int l, int u) {
    if (l < u) {
        int mid = (l + u) / 2;

        mergesort(arr, l, mid);
        mergesort(arr, mid + 1, u);

        merge(arr, l, mid, u);
    }
}

void sort(int a[], int l, int u) {
    int temp;
    for (int i = l + 1; i <= u; i++) {
        for (int j = i; j < u; i++) {
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n, n_peaks, temp;

    std::cout << "Enter array size: ";
    std::cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    std::cout << "Enter number of peaks: ";
    std::cin >> n_peaks;

    int peaks[n_peaks];
    for (int i = 0; i < n_peaks; i++) {
        std::cin >> arr[i];
    }

    int prev_peak = 0, cur_peak;
    for (int i = 0; i < n_peaks; i++) {
        cur_peak = i;
        sort(arr, prev_peak, cur_peak);
        prev_peak = cur_peak;
    }

    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }

    return 0;
}
