// https://leetcode.com/problems/longest-increasing-subsequence/
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[][] memo = new int[nums.length + 1][nums.length];
        
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return lengthOfLIS(nums, 0, -1, memo);
    }
    
    private int lengthOfLIS(int[] nums, int index, int prevIndex, int[][] memo) {
        if (index == nums.length) {
            return 0;
        }
        
        if (memo[prevIndex + 1][index] != -1) {
            return memo[prevIndex + 1][index];
        }
        
        int currentLength = 0;
        if (prevIndex < 0 || nums[index] > nums[prevIndex]) {
            currentLength = 1 + lengthOfLIS(nums, index + 1, index, memo);
        }
        
        return memo[prevIndex + 1][index] = Math.max(currentLength,
                                                 lengthOfLIS(nums, index + 1, prevIndex, memo));
    }
}
