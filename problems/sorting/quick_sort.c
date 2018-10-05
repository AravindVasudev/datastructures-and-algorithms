#include<stdio.h>

void swap(int* a, int* b) { // swaps a and b
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
  int pivot = arr[high]; // set pivot as rightmost element
  int i = low - 1;
  int j;

  for(j = low; j <= high - 1; j++) {
    // if the current element is less than pivot, increment i then swap i and j
    if(arr[j] <= pivot) {
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i + 1], &arr[high]); // i + 1 is the correct pivot position
  return i + 1;
}

int quick_sort(int arr[], int low, int high) {
  if(low < high) {
    int pi = partition(arr, low, high); // get the correct pivot position

    quick_sort(arr, low, pi - 1); // quick sort pivot left array
    quick_sort(arr, pi + 1, high); // quick sort pivot right array
  }
}

int main() {
  int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int arr_size = sizeof(arr) / sizeof(arr_size);
  int i;

  quick_sort(arr, 0, arr_size - 1);

  for (i = 0; i < arr_size; i++) {
    printf("%d ", arr[i]);
  }
}
