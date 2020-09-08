// https://leetcode.com/problems/3sum-smaller/
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int sum = 0;
        
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                if (nums[left] + nums[right] < target - nums[i]) {
                    sum += 1;
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return sum;
    }
}
