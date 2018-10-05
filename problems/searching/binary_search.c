#include<stdio.h>

int binary_search(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l) / 2;

    if(arr[mid] == x) return mid;
    if(arr[mid] > x) return binary_search(arr, l, mid - 1, x);
    return binary_search(arr, mid + 1, r, x);
  }
  return -1;
}

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int arr_size = sizeof(arr) / sizeof(arr_size);
  int ele1 = 3;
  int ele2 = 11;

  printf("Search 3: %d\n", binary_search(arr, 0, arr_size - 1, ele1));
  printf("Search 11: %d\n", binary_search(arr, 0, arr_size - 1, ele2));

}
