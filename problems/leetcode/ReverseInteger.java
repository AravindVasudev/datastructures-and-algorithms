class Solution {
    public int reverse(int x) {
      boolean isNeg = x < 0;
      x = Math.abs(x);

      int rev = 0;
      while (x > 0) {
        int digit = x % 10;
        int newrev = (rev * 10) + digit;

        if (rev != (newrev / 10)) {
          return 0;
        }

        rev = newrev;
        x /= 10;

      }

      if (isNeg) rev = -rev;

      return rev;
    }
}
