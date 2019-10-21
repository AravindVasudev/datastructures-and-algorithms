class Solution {
    public int rob(int[] nums) {
      if (nums.length == 0) {
        return 0;
      }

      if (nums.length == 1) {
        return nums[0];
      }

      if (nums.length == 2) {
        return Math.max(nums[0], nums[1]);
      }

      int N = nums.length;
      int prev1Max = Math.max(nums[0], nums[1]);
      int prev2Max = nums[0];
      int curMax = 0, max = 0;

      for (int i = 2; i < N; i++) {
        curMax = Math.max(prev2Max + nums[i], prev1Max);

        if (curMax > max) {
          max = curMax;
        }

        prev2Max = prev1Max;
        prev1Max = curMax;
      }

      return max;
    }
}
