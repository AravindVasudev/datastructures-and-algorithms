#include<stdio.h>

void merge(int arr[], int l, int m, int r) {
  int i, j, k;
  int n1 = m - l + 1; // size of left array
  int n2 = r - m; // size of right array

  // create temporary array to store the divided left and right array
  int L[n1], R[n2];
  for (i = 0; i < n1; i++) {
    L[i] = arr[l + i];
  }
  for (j = 0; j < n2; j++) {
    R[j] = arr[m + 1 + j];
  }

  // starting positions of arrays
  i = 0;
  j = 0;
  k = l;

  // Perform merge on sorted left and right array into the original array
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  // insert the remaining left array elements, if any
  while (i < n1) {
    arr[k] = L[i];
    i++; k++;
  }

  // insert the remaining right array elements, if any
  while (j < n2) {
    arr[k] = R[j];
    j++; k++;
  }
}

void merge_sort(int arr[], int l, int r) {
  if (l < r) {
    int m = (l + r) / 2; // middle position

    // Recursively split the array
    merge_sort(arr, l, m);
    merge_sort(arr, m + 1, r);

    // Merge the sorted arrays
    merge(arr, l, m, r);
  }
}

int main() {
  int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int arr_size = sizeof(arr) / sizeof(arr_size);
  int i;

  merge_sort(arr, 0, arr_size - 1);

  for (i = 0; i < arr_size; i++) {
    printf("%d ", arr[i]);
  }
}
