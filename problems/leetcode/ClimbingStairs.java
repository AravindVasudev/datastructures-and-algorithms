class Solution {
  public int climbStairs(int n) {
    if (n < 4) {
      return n;
    }

    int prev1 = 3, prev2 = 2, cur = 0;
    for (int i = 3; i < n; i++) {
      cur = prev1 + prev2;

      prev2 = prev1;
      prev1 = cur;
    }

    return cur;
  }
}
