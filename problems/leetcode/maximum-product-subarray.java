// https://leetcode.com/problems/maximum-product-subarray/
class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int maxProduct = nums[0];
        int minProduct = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            int temp = Math.max(nums[i], Math.max(maxProduct * nums[i], minProduct * nums[i]));
            minProduct = Math.min(nums[i], Math.min(maxProduct * nums[i], minProduct * nums[i]));
            
            maxProduct = temp;
            result = Math.max(result, maxProduct);
        }
        
        return result;
    }
}
