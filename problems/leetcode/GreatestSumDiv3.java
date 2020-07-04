// https://leetcode.com/problems/greatest-sum-divisible-by-three/
class Solution {
    public int maxSumDivThree(int[] nums) {
        int[] dp = new int[3];
        dp[1] = dp[2] = Integer.MIN_VALUE;

        for (int x : nums) {
            int[] dpNext = new int[3];
            dpNext[0] = Math.max(dp[x % 3] + x, dp[0]);
            dpNext[1] = Math.max(dp[(x + 1) % 3] + x, dp[1]);
            dpNext[2] = Math.max(dp[(x + 2) % 3] + x, dp[2]);

            dp = dpNext;
        }

        return dp[0];
    }
}
