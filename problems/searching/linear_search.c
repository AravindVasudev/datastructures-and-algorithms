#include<stdio.h>

int linear_search(int arr[], int arr_size, int ele) {
  int i = 0;
  for (i = 0; i < arr_size; i++) {
    if (arr[i] == ele) return i;
  }
  return -1;
}

int main() {
  int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int arr_size = sizeof(arr) / sizeof(arr_size);
  int ele1 = 3;
  int ele2 = 11;

  printf("Search 3: %d\n", linear_search(arr, arr_size, ele1));
  printf("Search 11: %d\n", linear_search(arr, arr_size, ele2));

}
