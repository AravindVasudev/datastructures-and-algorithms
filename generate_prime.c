#include <stdio.h>
#include <math.h>

int is_prime(int n) {
  int i, r = sqrt(n);
  for (int i = 2; i <= r; i++) {
    if (!(n % i)) return 0;
  }
  return 1;
}

int main() {
  int t, m, n;

  scanf("%d", &t);
  while (t--) {
    scanf("%d %d", &m, &n);
    if (m == 1) m++;
    for (; m <= n; m++) {
      if (is_prime(m)) printf("%d\n", m);
    }
    printf("\n");
  }
}
