// https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int left = 0, right = 0, sum = 0, minLen = Integer.MAX_VALUE;

        while (right < nums.length) {
            sum += nums[right++];
            
            while (sum >= s) {
                minLen = Math.min(minLen, right - left);
                sum -= nums[left++];
            }
        }
        
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
