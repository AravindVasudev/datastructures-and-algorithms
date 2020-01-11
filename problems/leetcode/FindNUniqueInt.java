// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
class Solution {
    public int[] sumZero(int n) {
        int range = n / 2;
        boolean isEven = n % 2 == 0;

        int[] ans = new int[n];
        int top = 0;

        for (int i = -range; i <= range; i++) {
            if (i == 0 && isEven) {
                continue;
            }

            ans[top++] = i;
        }

        return ans;
    }
}
